import hashlib
import os
import random

from django.conf import settings
from django.shortcuts import redirect
from inertia import InertiaResponse
from threading import Thread

from core.ai_service import generate_questions
from core.forms import QuizGenerationForm
from core.helpers import extract_images, get_relative_path, upload_file
from core.models import Document, DocumentImage, Quiz, QuizAttempt


def error(req, errors: dict, status=422):
    return InertiaResponse(req, "Dashboard/Start", {"errors": errors}, status=status)


def handle(request):
    form = QuizGenerationForm(request.POST, request.FILES)

    if form.is_valid() == False:
        flat = {field: ", ".join(errs) for field, errs in form.errors.items()}
        return error(request, flat, status=422)

    uploaded_document = request.FILES["document"]

    content = uploaded_document.read()
    content_hash = hashlib.sha256(content).hexdigest()
    uploaded_document.seek(0)

    existing = Document.objects.filter(
        user=request.user, content_hash=content_hash
    ).first()
    if existing:
        return error(
            request,
            dict(
                document="You have uploaded this document before. You may generate a new quiz by visiting here"
            ),
        )

    rel_path = upload_file(uploaded_document, "documents")
    abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)
    images = extract_images(abs_path, random.randint(10000000, 99999999))

    if not images:
        return error(
            request,
            {
                "document": "No images could be extracted from the file. It could be a scanned document."
            },
        )

    document = Document.objects.create(
        user=request.user,
        title=uploaded_document.name,
        file=rel_path,
        content_hash=content_hash,
    )

    for image in images:
        DocumentImage.objects.create(
            document=document,
            file_path=get_relative_path(image),
        )

    quiz = Quiz.objects.create(
        document=document, user=request.user, quiz_type=form.cleaned_data["quiz_type"]
    )

    quiz_attempt = QuizAttempt.objects.create(
        user=request.user,
        quiz=quiz,
        thinking_effort=form.cleaned_data["thinking_effort"],
        difficulty=form.cleaned_data["difficulty"],
    )

    document_images = list(document.document_images.all())
    Thread(target=generate_questions, args=(document_images, quiz_attempt)).start()

    return redirect(f"/quiz/{quiz_attempt.reference}")
