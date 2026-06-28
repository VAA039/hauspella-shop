from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    """
    Список товаров.
    """

    products = Product.objects.all()

    return render(
        request,
        "catalog/product_list.html",
        {
            "products": products,
        },
    )


def product_detail(request, pk):
    """
    Карточка товара.
    """

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
        },
    )