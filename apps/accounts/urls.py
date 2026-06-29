from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "",
        views.profile,
        name="profile",
    ),

    path(
        "profile/",
        views.profile_edit,
        name="profile_edit",
    ),
]