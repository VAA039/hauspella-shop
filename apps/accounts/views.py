from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserProfileForm

@login_required
def profile(request):
    """
    Личный кабинет пользователя.
    """

    return render(
        request,
        "accounts/profile.html",
        {
            "user": request.user,
            "orders_count": request.user.orders.count(),
            "wishlist_count": 0,
            "profile_completed": False,
        },
    )

@login_required
def profile_edit(request):
    """
    Страница редактирования профиля пользователя.
    """

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            return redirect(
                "accounts:profile",
            )

    else:

        form = UserProfileForm(
            instance=request.user,
        )

    return render(
        request,
        "accounts/profile_edit.html",
        {
            "form": form,
        },
    )