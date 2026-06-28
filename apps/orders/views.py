from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.cart.services import CartService

from .services import OrderService

@login_required
def checkout(request):
    """
    Страница подтверждения заказа.
    """

    cart = CartService.get_or_create_cart(
        request.user,
    )

    if not cart.items.exists():
        return redirect("cart:detail")

    return render(
        request,
        "orders/checkout.html",
        {
            "cart": cart,
        },
    )


@login_required
def confirm_order(request):
    """
    Подтвердить оформление заказа.
    """

    if request.method != "POST":
        return redirect("orders:checkout")

    OrderService.create_order(
        request.user,
    )

    return redirect("orders:success")

@login_required
def success(request):
    """
    Страница успешного оформления заказа.
    """

    return render(
        request,
        "orders/success.html",
    )