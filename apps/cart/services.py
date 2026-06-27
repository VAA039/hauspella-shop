from django.db import transaction

from .models import Cart


class CartService:
    """
    Сервис для работы с корзиной пользователя.
    """

    @staticmethod
    @transaction.atomic
    def get_or_create_cart(user):
        """
        Получить корзину пользователя или создать новую.
        """

        cart, created = Cart.objects.get_or_create(
            user=user,
        )

        return cart