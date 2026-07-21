import json
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseForbidden

from core.models import Answer, Option, QuizAttempt


class QuizController(LoginRequiredMixin, View):
    def post(self, request: HttpRequest, attempt_reference):
        data = json.loads(request.body)
        quiz_attempt = QuizAttempt.objects.filter(reference=attempt_reference)
        attempt = quiz_attempt.first()

        if not attempt:
            return redirect(reverse("start"))

        if attempt.user != request.user:
            return HttpResponseForbidden()

        print(attempt.started_at)
        if attempt.started_at is None:
            quiz_attempt.update(started_at=timezone.now())

        current_index = data.get("current_index")
        if current_index:
            quiz_attempt.update(current_index=current_index)

        question_id = data.get("question_id")
        option_id = data.get("option_id")
        save_answer(attempt, question_id, option_id)

        submitting = data.get("submitting")

        if submitting is True:
            quiz_attempt.update(completed_at=timezone.now())
            return redirect(
                reverse("quiz_summary", kwargs={"attempt_reference": attempt.reference})
            )

        return redirect(
            reverse(
                "start_quiz",
                kwargs={
                    "attempt_reference": attempt.reference,
                },
            )
        )


def save_answer(quiz_attempt: QuizAttempt, question_id, option_id):
    quiz_attempt = quiz_attempt

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
