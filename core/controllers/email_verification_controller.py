import json
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from allauth.account.models import EmailAddress
from allauth.account.internal.flows.email_verification import (
    send_verification_email_to_address,
)
from django.shortcuts import redirect

from core.logger import info


class RequestNewCodeView(View):
    def post(self, request):

        pending_state = request.session.get("account_login")
        email = pending_state["email"]
        if not email:
            return JsonResponse(
                {
                    "status": 400,
                    "errors": [
                        {"param": "email", "message": "This field is required."}
                    ],
                },
                status=400,
            )

        address = EmailAddress.objects.filter(
            email__iexact=email, verified=False
        ).first()
        if address:
            send_verification_email_to_address(request, address, signup=True)
            return JsonResponse({"status": 200, "data": {"sent": True}})

        return redirect(reverse("login"))
