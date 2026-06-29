from django import forms

from .models import User


class UserProfileForm(forms.ModelForm):
    """
    Форма редактирования профиля пользователя.
    """

    class Meta:
        model = User

        fields = (
            "first_name",
            "last_name",
        )

        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                },
            ),
        }