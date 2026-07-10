import os
import tempfile

from core.models import Setting
from django.conf import settings
from pathlib import Path
from typing import List


def get_setting(key, default=None):
    try:
        return Setting.objects.get(key=key).value
    except Setting.DoesNotExist:
        return default


def upload_file(f, folder=None):
    subdir = os.path.join("uploads", folder) if folder else "uploads"
    dest = os.path.join(settings.MEDIA_ROOT, subdir)
    os.makedirs(dest, exist_ok=True)
    file_path = os.path.join(dest, f.name)
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    print(file_path)
    return file_path

def extract_images(
    file_path: str,
    output_dir: str | None = None,
    min_width: int = 100,
    min_height: int = 100,
) -> List[str]:
    """
    Extracts images from a single PDF, PPTX, or DOCX file.
    Filters out images smaller than min_width/min_height.

    Returns:
        List of absolute paths to the saved image files.
    """
    file_path = Path(file_path).resolve()
    output_dir = Path(output_dir or settings.MEDIA_ROOT / "extracted_images")
    output_dir.mkdir(parents=True, exist_ok=True)