import base64
import os
from pathlib import Path
from typing import List
from openai import OpenAI
from core.helpers import extract_text
from core.logger import info
from core.models import DocumentImage, Option, Question, Quiz, QuizAttempt
from django.conf import settings
import time
from partial_json_parser import loads


def generate_questions(
    document_images: List[DocumentImage],
    quiz_attempt: QuizAttempt,
) -> List[Question]:
    quiz = quiz_attempt.quiz
    document = quiz.document
    file_path = document.file.replace("\\", "/")
    absolute_path = Path(settings.MEDIA_ROOT) / file_path

    document_text = extract_text(absolute_path)

    image_blocks = []
    for document_image in document_images:
        image_absolute_path = Path(settings.MEDIA_ROOT) / document_image.file_path
        with open(image_absolute_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode("utf-8")
        image_blocks.append(
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{encoded}",
            }
        )

    from threading import Thread

    api_key = os.getenv("QWEN_API_KEY")
    base_url = os.getenv("QWEN_URL")
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    Thread(
        target=generate_reasoning,
        args=(client, image_blocks, quiz_attempt, document_text),
    ).start()

    stream = client.responses.create(
        model="qwen3.7-plus",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Generate 2 multiple-choice questions per image based on visual findings. "
                        "Align questions with the document text when applicable.\n\n"
                        f"Document Text: {document_text}\n\n"
                        f"Images: {len(document_images)}\n"
                        f"Difficulty Level: {quiz_attempt.difficulty}\n"
                        "Rules: 4 options per question (1 correct, 3 incorrect), image_index to reference images, "
                        "valid JSON only, no markdown, hide is_correct.\n"
                        "CRITICAL: Never include phrases like 'mentioned in the text' or 'according to the document'.\n"
                        '{"questions": [{"image_index": 0, "text": "...", "options": [{"text": "...", "is_correct": true}, {"text": "...", "is_correct": false}, {"text": "...", "is_correct": false}, {"text": "...", "is_correct": false}]}]}',
                    },
                    *image_blocks,
                ],
            }
        ],
        stream=True,
        reasoning={"effort": "none"},
    )

    stream_buffer = ""
    emitted_count = 0

    for event in stream:
        if event.type == "response.output_text.delta":
            stream_buffer += event.delta
            emitted_count, new_questions = extract_complete_questions_from_stream(
                stream_buffer, emitted_count
            )

            for question_data in new_questions:
                image_index = question_data["image_index"]
                image_identifier = document_images[image_index]
                question = Question.objects.create(
                    quiz=quiz,
                    image=image_identifier,
                    text=question_data["text"],
                )
                for option_data in question_data["options"]:
                    Option.objects.create(
                        question=question,
                        text=option_data["text"],
                        is_correct=option_data["is_correct"],
                    )

    quiz_attempt.questions_generated = True
    quiz_attempt.save()
    return


def generate_reasoning(client, image_blocks, quiz_attempt, document_text):
    reasoning_effort = "low" if quiz_attempt.thinking_effort == "thinking" else "none"
    stream = client.responses.create(
        model="qwen3.7-plus",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Analyze these medical images in detail. Describe your findings, "
                        "what you observe, and your diagnostic thinking. "
                        f"Reference this document text when relevant: {document_text}\n"
                        "Do NOT generate questions.",
                    },
                    *image_blocks,
                ],
            }
        ],
        stream=True,
        reasoning={"effort": reasoning_effort},
    )

    reasoning_text = ""
    for event in stream:
        if event.type == "response.output_text.delta":
            reasoning_text += event.delta

    if reasoning_text:
        quiz_attempt.reasoning = reasoning_text
        quiz_attempt.save(update_fields=["reasoning"])


def extract_complete_questions_from_stream(stream_buffer, emitted_count):
    try:
        data = loads(stream_buffer)
        questions = data.get("questions", [])
        new_questions = []
        for question in questions[emitted_count:]:
            if (
                "image_index" in question
                and "text" in question
                and "options" in question
            ):
                options = question["options"]
                if len(options) == 4 and all(
                    isinstance(option, dict)
                    and option.get("text")
                    and "is_correct" in option
                    for option in options
                ):
                    new_questions.append(question)
        return emitted_count + len(new_questions), new_questions
    except Exception as error:
        return emitted_count, []
