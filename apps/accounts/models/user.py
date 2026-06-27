from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.managers.user_manager import UserManager


class User(AbstractUser):
    """
    Пользователь платформы HAUSPELLA.
    """

    username = None

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        blank=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email