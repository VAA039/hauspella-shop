from django.db import models

from .product import Product


class ProductVideo(models.Model):
    """
    Логическое видео товара.

    Одно видео может иметь несколько источников публикации.
    """

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    # ------------------------------------------------------------------
    # Content
    # ------------------------------------------------------------------


    title = models.CharField(
        verbose_name="Название видео",
        max_length=255,
        help_text="Название, которое будет отображаться покупателю.",
    )

    # ------------------------------------------------------------------
    # Service
    # ------------------------------------------------------------------

    sort_order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
        help_text="Чем меньше число, тем выше видео в списке.",
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Видео товара"
        verbose_name_plural = "Видео товаров"
        ordering = (
            "sort_order",
            "id",
        )

    def __str__(self):
        return f"{self.product.article} — {self.title}"