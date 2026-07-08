import random
from django.core.management.base import BaseCommand
from core.models import QuizType
from faker import Faker


class Command(BaseCommand):
    help = "Seeds the database with initial mock data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        QuizType.objects.create(
            name="MCQ",
            slug="mcq",
        )

        QuizType.objects.create(
            name="Open ended",
            slug="open-ended",
        )

        self.stdout.write(self.style.SUCCESS("Database seeding completed."))
