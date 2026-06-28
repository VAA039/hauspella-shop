from django.http import HttpResponse


def cart_detail(request):
    """
    Страница корзины.
    """

    return HttpResponse("Корзина HAUSPELLA")