from logging import info
import os
from typing import List
import zipfile

import fitz


def extract_office(document_path: str, output_dir: str | None, type: str) -> List[str]:

    extracted_images = []

    medialocation = "ppt" if type == "pptx" else "word"
    with zipfile.ZipFile(document_path, "r") as archive:
        for file_info in archive.infolist():
            if file_info.filename.startswith(f"{medialocation}/media"):
                image_data = archive.read(file_info.filename)
                original_name = os.path.basename(file_info.filename)
                save_path = os.path.join(output_dir, f"extracted_{original_name}")

                with open(save_path, "wb") as img_file:
                    img_file.write(image_data)

                extracted_images.append(save_path)

    return extracted_images


def _is_scanned(pdf_document: fitz.Document) -> bool:
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        text = page.get_text().strip()
        if len(text) > 50:
            return False
    return True


def extract_pdf(document_path: str, output_dir: str | None):
    image_paths = []

    pdf_document = fitz.open(document_path)

    if _is_scanned(pdf_document):
        pdf_document.close()
        return []

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]

        image_list = page.get_images(full=True)

        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]

            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_name = f"page_{page_number + 1}_img_{img_index + 1}.{image_ext}"
            image_path = os.path.join(output_dir, image_name)

            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

            image_paths.append(image_path)

    pdf_document.close()
    return image_paths
