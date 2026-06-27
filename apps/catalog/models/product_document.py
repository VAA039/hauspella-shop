from django.db import models
from django.core.validators import FileExtensionValidator

from .product import Product
from ..utils.upload_paths import product_document_upload_path


class ProductDocumentType(models.TextChoices):
    """
    Тип документа товара.
    """

    INSTRUCTION = "instruction", "Инструкция"
    CERTIFICATE = "certificate", "Сертификат"
    DECLARATION = "declaration", "Декларация"
    DATASHEET = "datasheet", "Техническая спецификация"
    WARRANTY = "warranty", "Гарантия"
    SAFETY = "safety", "Документ по безопасности"
    OTHER = "other", "Другое"


class ProductDocumentLanguage(models.TextChoices):
    """
    Язык документа.
    """

    RUSSIAN = "ru", "Русский"
    ENGLISH = "en", "English"

    KAZAKH = "kk", "Қазақша"
    UZBEK = "uz", "O'zbek"
    KYRGYZ = "ky", "Кыргызча"
    ARMENIAN = "hy", "Հայերեն"
    GEORGIAN = "ka", "ქართული"
    BELARUSIAN = "be", "Беларуская"

    GERMAN = "de", "Deutsch"
    FRENCH = "fr", "Français"
    ITALIAN = "it", "Italiano"
    SPANISH = "es", "Español"
    POLISH = "pl", "Polski"

    CHINESE = "zh", "中文"

    OTHER = "other", "Другое"


class ProductDocument(models.Model):
    """
    Документ товара.

    Один товар может иметь неограниченное количество документов.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="documents",
    )


    # ------------------------------------------------------------------
    # Content
    # ------------------------------------------------------------------

    title = models.CharField(
        verbose_name="Название документа",
        max_length=255,
        help_text="Название, которое будет отображаться пользователю.",
    )

    file = models.FileField(
        verbose_name="PDF-документ",
        validators=[
        FileExtensionValidator(
            allowed_extensions=["pdf"],
        ),
    ],
        upload_to=product_document_upload_path,
    )


    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    document_type = models.CharField(
        verbose_name="Тип документа",
        max_length=20,
        choices=ProductDocumentType.choices,
        default=ProductDocumentType.OTHER,
    )

    language = models.CharField(
        verbose_name="Язык документа",
        max_length=10,
        choices=ProductDocumentLanguage.choices,
        default=ProductDocumentLanguage.RUSSIAN,
    )



    # ------------------------------------------------------------------
    # Service
    # ------------------------------------------------------------------

    sort_order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
        help_text="Чем меньше число, тем выше документ в списке.",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )


    class Meta:
        verbose_name = "Документ товара"
        verbose_name_plural = "Документы товаров"
        ordering = (
            "sort_order",
            "id",
        )


    def __str__(self):
        return f"{self.product.article} — {self.title}"
    


