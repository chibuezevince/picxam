from django.shortcuts import redirect
from inertia import render as inertia_render
from core.forms import QuizGenerationForm
from core.helpers import extract_images, upload_file


def handle(request):
    form = QuizGenerationForm(request.POST, request.FILES)

    if form.is_valid():
        document = form.cleaned_data["document"]
        questions_count = form.cleaned_data["questions_count"]
        quiz_type = form.cleaned_data["quiz_type"]

        uploaded_document = request.FILES["document"]
        print(uploaded_document)

        images = extract_images(upload_file(uploaded_document, "documents"))
        print(images)
        return redirect("/dashboard")

    errors = {field: ", ".join(errs) for field, errs in form.errors.items()}
    return inertia_render(
        request,
        "Dashboard/Start",
        {"errors": errors},
        status=422,
    )
