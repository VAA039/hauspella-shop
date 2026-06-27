from django.conf import settings
from django.db import models


class Cart(models.Model):
    """
    Корзина пользователя.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="cart",
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
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
        ordering = ("-updated_at",)

    def __str__(self):
        return f"Корзина пользователя {self.user.email}"
        
    @property
    def items_count(self):
        """
        Общее количество товаров в корзине.
        """
        return sum(item.quantity for item in self.items.all())


    @property
    def total_price(self):
        """
        Общая стоимость корзины.
        """
        return sum(
            item.quantity * item.product.price
            for item in self.items.all()
        )