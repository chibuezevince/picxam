import random
from django.core.management.base import BaseCommand
from core.models import QuizType, Setting
from faker import Faker


class Command(BaseCommand):
    help = "Seeds the database with initial mock data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # QuizType.objects.create(
        #     name="MCQ",
        #     slug="mcq",
        # )

        # QuizType.objects.create(
        #     name="Open ended",
        #     slug="open-ended",
        # )

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
        
        Setting.objects.create(
            key="ilovepdf_public_key",
            value="project_public_20cb753803cce71edda6d714e6931b8f_z-dFvff4a2a6bedd3b70da09f651e95bc9fb9",
        )
        
        Setting.objects.create(
            key="ilovepdf_secret_key",
            value="secret_key_ec5c267382d5c53b59bf9f9c1c1cb9bf_sCdVw6d0ae4ba169e43d1c9a85401f956d8c4",
        )

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
