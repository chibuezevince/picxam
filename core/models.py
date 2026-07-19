from random import choice
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = None

    name = models.CharField(max_length=255, blank=False, verbose_name="Full Name")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password"]

    def __str__(self):
        return self.name


class Document(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=255)
    file = models.TextField()
    content_hash = models.CharField(max_length=64, blank=True, editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuizType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Quiz(models.Model):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="quizzes"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="quizzes"
    )
    quiz_type = models.ForeignKey(
        QuizType, on_delete=models.CASCADE, related_name="quizzes"
    )


class QuizAttempt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="quiz_attempts"
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="quiz_attempts"
    )
    score = models.IntegerField(null=True, blank=True)
    current_index = models.IntegerField(default=1, blank=False)
    is_completed = models.BooleanField(default=False)
    questions_generated = models.BooleanField(default=False)
    reasoning = models.TextField(blank=True, default="")
    started_at = models.DateTimeField(null=True, blank=True)
    reference = models.UUIDField(default=uuid.uuid4, editable=False)

    class ThinkingEffort(models.Choices):
        Thinking = "thinking"
        NonThinking = "non-thinking"

    thinking_effort = models.CharField(
        max_length=15,
        choices=ThinkingEffort.choices,
        default=ThinkingEffort.Thinking,
    )

    class Difficulty(models.Choices):
        Medium = "medium"
        Hard = "hard"

    difficulty = models.CharField(
        max_length=8,
        choices=Difficulty.choices,
        default=Difficulty.Medium,
    )

    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DocumentImage(models.Model):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document_images"
    )
    file_path = models.TextField()
    hash = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Image {self.id} for Document {self.document_id}"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    image = models.ForeignKey(
        DocumentImage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="questions",
    )
    text = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)


class Option(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    text = models.TextField()
    is_correct = models.BooleanField()


class Answer(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="answers"
    )
    quiz_attempt = models.ForeignKey(
        QuizAttempt, on_delete=models.CASCADE, related_name="answers"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    option = models.ForeignKey(
        Option, on_delete=models.CASCADE, null=True, blank=True, related_name="answers"
    )
    text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "question"], name="unique_user_question"
            ),
        ]


class Setting(models.Model):
    key = models.CharField(unique=True, max_length=100)
    value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
