from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .services import OrderService


@login_required
def checkout(request):
    """
    Оформить заказ.
    """

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