from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.catalog.models import Product
from apps.cart.services import CartService

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


@login_required
def add_to_cart(request, product_id):
    """
    Добавить товар в корзину.
    """

    product = get_object_or_404(
        Product,
        pk=product_id,
    )

    CartService.add_product(
        request.user,
        product,
    )

    return redirect("cart:detail")





