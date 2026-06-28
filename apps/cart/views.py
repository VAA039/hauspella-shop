from django.shortcuts import render

from apps.cart.services import CartService

from django.contrib.auth.decorators import login_required


@login_required
def cart_detail(request):
    """
    Страница корзины.
    """

    cart = CartService.get_or_create_cart(
        request.user,
    )

    return render(
        request,
        "cart/cart_detail.html",
        {
            "cart": cart,
        },
    )

