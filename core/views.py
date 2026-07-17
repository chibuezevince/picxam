from inertia import inertia, render as inertia_render
from django.contrib.auth.decorators import login_required
from core.controllers.quiz_generation_controller import handle
from core.middlewares import pending_required, guest_required
from inertia.http import encrypt_history
from django.db.models import Count
from core.models import Option, Question, QuizAttempt
from django.http import StreamingHttpResponse
import json


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


@inertia("Auth/ForgotPassword")
def forgot_password(request):
    return {}


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
    attempt = (
        QuizAttempt.objects.filter(reference=attempt_reference, user=request.user)
        .select_related("quiz__quiz_type")
        .prefetch_related("answers")
        .first()
    )
    return inertia_render(
        request,
        "Quiz/Index",
        {
            "quizAttempt": {
                "reference": attempt_reference,
                "quizType": attempt.quiz.quiz_type.name if attempt else None,
                "currentIndex": attempt.current_index,
                "answers": {
                    answer.question_id: answer.option_id
                    for answer in attempt.answers.all()
                },
            },
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

        while True:
            attempt = QuizAttempt.objects.get(id=attempt.id)
            questions = (
                attempt.quiz.questions.prefetch_related("options").all().order_by("id")
            )

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
                        for option in question.options.all()
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
