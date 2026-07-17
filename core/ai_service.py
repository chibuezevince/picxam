import os
from pathlib import Path
from typing import List
from openai import OpenAI
from core.helpers import extract_text
from core.models import Question, Quiz
from django.conf import settings


def generate_questions(quiz: Quiz) -> List[Question]:
    document = quiz.document
    media_url = str(settings.MEDIA_URL).replace("/", "")
    file_path = document.file.replace("\\", "/")
    absolute_path = Path(f"{media_url}/{file_path}")

    document_text = extract_text(absolute_path)
     
    api_key = os.getenv("QWEN_API_KEY")
    base_url = os.getenv("QWEN_URL")
    
    return



# import time

# starttime = time.perf_counter()
# client = OpenAI(
#     api_key=api_key,
#     base_url=base_url,
# )
# stream = client.responses.create(
#     model="qwen3.7-plus", input="Hello", stream=True, reasoning={"effort": "none"}
# )
# for event in stream:
#     if event.type == "response.output_text.delta":
#         print(event.delta, end="", flush=True)

# endtime = time.perf_counter()
# print("\n", endtime - starttime)

print()