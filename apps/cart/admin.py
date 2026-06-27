from django.contrib import admin

from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Администрирование корзин.
    """

    list_display = (
        "user",
        "items_count",
        "total_price",
        "updated_at",
    )

    search_fields = (
        "user__email",
    )

    ordering = (
        "-updated_at",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """
    Администрирование товаров в корзине.
    """

    list_display = (
        "cart",
        "product",
        "quantity",
        "total_price",
        "updated_at",
    )

    search_fields = (
        "product__name",
        "cart__user__email",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-updated_at",
    )