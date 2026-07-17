import json

from django.urls import reverse
from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest

from core.models import Answer, Option, Question, QuizAttempt


class QuizController(View):
    def post(self, request: HttpRequest, attempt_reference):
        data = json.loads(request.body)
        quiz_attempt = QuizAttempt.objects.filter(reference=attempt_reference).first()
        if not quiz_attempt:
            return redirect(reverse("start"))

        current_index = data.get("current_index")
        if current_index:
            QuizAttempt.objects.filter(reference=attempt_reference).update(
                current_index=current_index
            )

        question_id = data.get("question_id")
        option_id = data.get("option_id")
        if question_id and option_id is not None:
            option = Option.objects.get(id=option_id)
            Answer.objects.update_or_create(
                user=quiz_attempt.user,
                quiz_attempt=quiz_attempt,
                question_id=question_id,
                defaults={
                    "option_id": option_id,
                    "is_correct": option.is_correct,
                },
            )

        return redirect(reverse("start"))
