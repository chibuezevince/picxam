from django.urls import reverse
from django.shortcuts import redirect
from inertia import inertia, render as inertia_render
from django.contrib.auth.decorators import login_required
from core.controllers.quiz_generation_controller import handle
from core.logger import info
from core.middlewares import pending_required, guest_required
from inertia.http import encrypt_history
from django.db.models import Count
from core.models import Question, QuizAttempt
from django.http import Http404, StreamingHttpResponse
import json
import random


@inertia("Home")
def home(request):
    return {}


@inertia("Terms")
def terms(request):
    return {}


@inertia("Privacy")
def privacy(request):
    return {}


@guest_required()
@inertia("Auth/Login")
def login(request):
    return {}


@guest_required()
@inertia("Auth/Onboarding")
def onboarding(request):
    return {}


@pending_required
@guest_required()
@inertia("Auth/VerifyEmail")
def verify_email(request):
    return {}


@guest_required()
@inertia("Auth/ForgotPassword")
def forgot_password(request):
    return {}


@guest_required()
@inertia("Auth/ResetPassword")
def reset_password(request, key):
    return {"resetKey": key}


@login_required
@inertia("Dashboard/Index")
def dashboard(request):
    encrypt_history(request)
    return {
        "user": {
            "name": request.user.name,
            "email": request.user.email,
        },
        "documentsCount": lambda: request.user.documents.count(),
        "quizCount": lambda: request.user.quizzes.count(),
        "questionsCount": lambda: Question.objects.filter(
            quiz__user=request.user
        ).count(),
        "recentDocuments": request.user.documents.annotate(
            questions_count=Count("quizzes__questions"),
            quizzes_count=Count("quizzes", distinct=True),
        ).order_by("-created_at")[:5],
    }


@login_required
def start(request):
    if request.method == "POST":
        return handle(request)

    return inertia_render(request, "Dashboard/Start")


@login_required
def start_quiz(request, attempt_reference):

    attempt = QuizAttempt.objects.filter(
        reference=attempt_reference, user=request.user
    ).first()

    if attempt is None:
        raise Http404()

    attempt = (
        QuizAttempt.objects.filter(reference=attempt_reference, user=request.user)
        .select_related("quiz__quiz_type")
        .prefetch_related("answers")
        .first()
    )

    if attempt.completed_at is not None:
        return redirect(
            reverse("quiz_summary", kwargs={"attempt_reference": attempt.reference})
        )

    quiz = attempt.quiz
    return inertia_render(
        request,
        "Quiz/Index",
        {
            "quizAttempt": {
                "reference": attempt_reference,
                "quizType": quiz.quiz_type.name if attempt else None,
                "currentIndex": attempt.current_index,
                "reasoning": attempt.reasoning or "",
                "answers": {
                    answer.question_id: answer.option_id
                    for answer in attempt.answers.all()
                },
            },
            "questions": [
                {
                    "id": question.id,
                    "text": question.text,
                    "image": question.image.file_path if question.image else None,
                    "options": [
                        {"id": option.id, "text": option.text}
                        for option in random.sample(
                            list(question.options.all()),
                            question.options.count(),
                        )
                    ],
                }
                for question in quiz.questions.all()
            ],
        },
    )


@login_required
def stream_questions(request, attempt_reference):
    def event_stream():
        import time

        attempt = QuizAttempt.objects.filter(
            reference=attempt_reference, user=request.user
        ).first()

        if not attempt:
            yield f"data: {json.dumps({'type': 'error', 'message': 'Attempt not found'})}\n\n"
            return

        yield f"data: {json.dumps({'type': 'connected'})}\n\n"

        sent_ids = set()
        sent_reasoning = ""

        while True:
            attempt = QuizAttempt.objects.get(id=attempt.id)
            questions = (
                attempt.quiz.questions.prefetch_related("options").all().order_by("id")
            )

            if attempt.reasoning and attempt.reasoning != sent_reasoning:
                new_part = attempt.reasoning[len(sent_reasoning) :]
                sent_reasoning = attempt.reasoning
                yield f"data: {json.dumps({'type': 'reasoning', 'text': new_part})}\n\n"

            for question in questions:
                if question.id in sent_ids:
                    continue
                sent_ids.add(question.id)
                payload = {
                    "id": question.id,
                    "text": question.text,
                    "image": question.image.file_path if question.image else None,
                    "imageHash": str(question.image.hash) if question.image else None,
                    "options": [
                        {"id": option.id, "text": option.text}
                        for option in random.sample(
                            list(question.options.all()),
                            question.options.count(),
                        )
                    ],
                    "generated": len(sent_ids),
                }
                yield f"data: {json.dumps(payload)}\n\n"

            if attempt.questions_generated:
                yield f"data: {json.dumps({'type': 'done'})}\n\n"
                return

            time.sleep(0.5)
            attempt.refresh_from_db()

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


@login_required
def quiz_summary(request, attempt_reference):
    attempt = (
        QuizAttempt.objects.filter(reference=attempt_reference, user=request.user)
        .select_related("quiz__quiz_type", "quiz__document")
        .prefetch_related(
            "answers__question__options",
            "answers__option",
            "quiz__questions__options",
        )
        .first()
    )

    if not attempt:
        raise Http404()

    questions_with_answers = []
    for question in attempt.quiz.questions.all():
        answer = attempt.answers.filter(question=question).first()
        questions_with_answers.append(
            {
                "id": question.id,
                "text": question.text,
                "image": question.image.file_path if question.image else None,
                "options": [
                    {
                        "id": option.id,
                        "text": option.text,
                        "isCorrect": option.is_correct,
                    }
                    for option in question.options.all()
                ],
                "selectedOptionId": answer.option_id if answer else None,
                "isCorrect": answer.is_correct if answer else None,
            }
        )

    return inertia_render(
        request,
        "Quiz/Summary",
        {
            "quizAttempt": {
                "reference": str(attempt.reference),
                "quizType": (
                    attempt.quiz.quiz_type.name if attempt.quiz.quiz_type else None
                ),
                "documentName": attempt.quiz.document.title,
                "difficulty": attempt.difficulty,
                "thinkingEffort": attempt.thinking_effort,
                "score": attempt.score,
                "correctCount": attempt.correct_count,
                "incorrectCount": attempt.incorrect_count,
                "totalQuestions": attempt.quiz.questions.count(),
                "startedAt": (
                    attempt.started_at.isoformat() if attempt.started_at else None
                ),
                "completedAt": (
                    attempt.completed_at.isoformat() if attempt.completed_at else None
                ),
            },
            "questions": questions_with_answers,
        },
    )
