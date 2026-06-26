from django.db import models

from .product import Product
from ..utils.upload_paths import product_image_upload_path


class ProductImageType(models.TextChoices):
    """
    Тип изображения товара.
    """

    MAIN = "main", "Главное"
    FRONT = "front", "Спереди"
    BACK = "back", "Сзади"
    DETAIL = "detail", "Деталь"
    INFOGRAPHIC = "infographic", "Инфографика"
    PACKAGE = "package", "Комплектация"
    LIFESTYLE = "lifestyle", "В интерьере"
    OTHER = "other", "Другое"


class ProductImage(models.Model):
    """
    Изображение товара.

    Один товар может иметь неограниченное количество изображений.
    """

    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="images",
    )


    # ------------------------------------------------------------------
    # Media
    # ------------------------------------------------------------------

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to=product_image_upload_path,
    )


    # ------------------------------------------------------------------
    # SEO
    # ------------------------------------------------------------------

    alt = models.CharField(
        verbose_name="ALT-текст",
        max_length=255,
        blank=True,
        help_text="Описание изображения для SEO и доступности.",
    )


    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    image_type = models.CharField(
        verbose_name="Тип изображения",
        max_length=20,
        choices=ProductImageType.choices,
        default=ProductImageType.OTHER,
    )

    sort_order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
        db_index=True,
        help_text="Чем меньше число, тем выше изображение в галерее.",
    )


    # ------------------------------------------------------------------
    # Service
    # ------------------------------------------------------------------

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
        ordering = (
            "sort_order",
            "id",
        )



    def __str__(self):
        return f"{self.product.article} — {self.get_image_type_display()}"


