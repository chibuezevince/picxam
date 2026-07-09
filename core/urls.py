from django.urls import path

from core.controllers.email_verification_controller import RequestNewCodeView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("terms", views.terms, name="terms"),
    path("privacy", views.privacy, name="privacy"),
    
    path("login", views.login, name="login"),
    path("onboarding", views.onboarding, name="onboarding"),
    path("email/verify", views.verify_email, name="verify_email"),
    path("auth/request-new-code", RequestNewCodeView.as_view(), name="request_new_code"),
    path("forgot-password", views.forgot_password, name="forgot_password"),
    path("reset-password/<str:key>/", views.reset_password, name="reset_password"),
    
    path("dashboard", views.dashboard, name="dashboard"),
    path("start", views.start, name="start"),
]
