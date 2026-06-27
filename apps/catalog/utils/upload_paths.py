from pathlib import Path

from django.utils.text import slugify




def product_image_upload_path(instance, filename):
    """
    Формирует путь для хранения изображения товара.

    Пример:

    media/
        products/
            HSP-000001/
                wall-mounted-clothes-dryer.jpg
    """

    extension = Path(filename).suffix.lower()

    product = instance.product

    file_name = f"{slugify(product.slug)}{extension}"

    return f"products/{product.article}/images/{file_name}"


def product_document_upload_path(instance, filename):
    """
    Формирует путь для хранения документа товара.

    Пример:

    media/
        products/
            HSP-000001/
                documents/
                    User Manual.pdf
    """

    product = instance.product

    return f"products/{product.article}/documents/{filename}"