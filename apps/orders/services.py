from django.db import transaction

from apps.cart.services import CartService
from .models import Order, OrderItem


class OrderService:
    """
    Сервис для работы с заказами.
    """

    @staticmethod
    @transaction.atomic
    def create_order(user):
        """
        Создать заказ пользователя.
        """

        cart = CartService.get_or_create_cart(user)

        if not cart.items.exists():
            raise ValueError("Корзина пуста.")
        

        order = Order.objects.create(
            user=user,
        )

        for cart_item in cart.items.all():

            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                price=cart_item.product.price,
                quantity=cart_item.quantity,
            )


        cart.items.all().delete()
        return order