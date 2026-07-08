from inertia import inertia
from django.contrib.auth.decorators import login_required
from core.middlewares import pending_required, guest_required
from inertia.http import encrypt_history

from core.models import QuizType


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
    return {"email": request.session.get("email")}


@inertia("Auth/ForgotPassword")
def forgot_password(request):
    return {}


@inertia("Auth/ResetPassword")
def reset_password(request, key):
    return {"resetKey": key}


@login_required
@inertia("Dashboard")
def dashboard(request):
    encrypt_history(request)
    return {
        "user": request.user,
        "documentCount": lambda: request.user.documents.count(),
        "quizCount": lambda: request.user.quizzes.count(),
        "documentsCount": lambda: request.user.documents.count(),
    }
