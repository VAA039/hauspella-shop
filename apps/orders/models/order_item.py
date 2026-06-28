from django.db import models

from apps.catalog.models import Product

from .order import Order


class OrderItem(models.Model):
    """
    Товар в заказе.
    """

    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.PROTECT,
        related_name="order_items",
    )

    price = models.DecimalField(
        verbose_name="Цена на момент покупки",
        max_digits=10,
        decimal_places=2,
    )

    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=1,
    )

    class Meta:
        verbose_name = "Товар заказа"
        verbose_name_plural = "Товары заказа"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"