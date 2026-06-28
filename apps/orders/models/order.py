from django.conf import settings
from django.db import models

class OrderStatus(models.TextChoices):
    """
    Статусы заказа.
    """

    NEW = "new", "Новый"
    PROCESSING = "processing", "В обработке"
    COMPLETED = "completed", "Завершён"
    CANCELLED = "cancelled", "Отменён"


class Order(models.Model):
    """
    Заказ пользователя.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    status = models.CharField(
        verbose_name="Статус",
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.NEW,
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
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("-created_at",)

    def __str__(self):
        return f"Заказ №{self.pk}"
    
    @property
    def total_price(self):
        """
        Общая стоимость заказа.
        """

        return sum(
            item.price * item.quantity
            for item in self.items.all()
        )