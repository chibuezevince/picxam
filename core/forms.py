import os

from django.core.exceptions import ValidationError

from django import forms
import magic
from core.helpers import get_setting
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import QuizType


class CustomSignupForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    agree = forms.BooleanField(required=True)

    def signup(self, request, user):
        user.name = self.cleaned_data["name"]
        user.save()


def validate_file_size(value):
    limitMB = get_setting("max_file_size")
    limit = limitMB * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f"File size cannot exceed {limitMB}")


def validate_file_extension(value):
    ALLOWED_MIMETYPES = get_setting("accepted_file_types")

    ext = os.path.splitext(value.name)[1].lower()
    if ext not in ALLOWED_MIMETYPES:
        raise ValidationError("Unsupported file format. Allowed: .pdf, .docx, .pptx")

    file_peek = value.read(2048)
    value.seek(0)
    actual_mime_type = magic.from_buffer(file_peek, mime=True)
    expected_mime_type = ALLOWED_MIMETYPES[ext]

    if actual_mime_type != expected_mime_type:
        raise ValidationError(
            "File content does not match its extension. Upload rejected."
        )


class QuizGenerationForm(forms.Form):
    document = forms.FileField(
        validators=[validate_file_size, validate_file_extension],
        required=True,
    )

    quiz_type = forms.ModelChoiceField(QuizType.objects.all(), to_field_name="slug")
