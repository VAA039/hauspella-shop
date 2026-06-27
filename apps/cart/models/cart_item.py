from django.db import models

from apps.catalog.models import Product

from .cart import Cart


class CartItem(models.Model):
    """
    Позиция товара в корзине.
    """

    cart = models.ForeignKey(
        Cart,
        verbose_name="Корзина",
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        verbose_name="Товар",
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    quantity = models.PositiveSmallIntegerField(
        verbose_name="Количество",
        default=1,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"
        ordering = (
            "-updated_at",
        )

        constraints = [
            models.UniqueConstraint(
                fields=("cart", "product"),
                name="unique_cart_product",
            ),
            models.CheckConstraint(
                condition=models.Q(quantity__gte=1),
                name="cart_item_quantity_gte_1",
            ),
        ]

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
    

    @property
    def total_price(self):
        """
        Стоимость позиции корзины.
        """
        return self.product.price * self.quantity
    
