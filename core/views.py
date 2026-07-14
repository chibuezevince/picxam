from inertia import inertia, render as inertia_render
from django.contrib.auth.decorators import login_required
from core.controllers.quiz_generation_controller import handle
from core.middlewares import pending_required, guest_required
from inertia.http import encrypt_history
from django.db.models import Count
from core.models import Question


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
    return inertia_render(request, "Quiz/Index")
