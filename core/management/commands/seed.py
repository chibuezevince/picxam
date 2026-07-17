import random
from django.core.management.base import BaseCommand
from core.models import QuizType, Setting
from faker import Faker


class Command(BaseCommand):
    help = "Seeds the database with initial mock data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        QuizType.objects.create(
            name="Multi Choice",
            slug="mcq",
        )

        QuizType.objects.create(
            name="Open ended",
            slug="open-ended",
        )

        Setting.objects.create(
            key="accepted_file_types",
            value={
                ".pdf": "application/pdf",
                ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            },
        )

        Setting.objects.create(
            key="max_file_size",
            value=10,
        )

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
