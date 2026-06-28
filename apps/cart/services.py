from django.db import transaction

from apps.catalog.models import Product

from .models import Cart, CartItem


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

    @staticmethod
    @transaction.atomic
    def add_product(user, product):
        """
        Добавить товар в корзину пользователя.
        """

        cart = CartService.get_or_create_cart(
            user,
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={
                "quantity": 1,
            },
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save(
                update_fields=("quantity", "updated_at"),
            )

        return cart_item