from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Категория товаров.
    Например:
        Дом
        Бытовая техника
        Электроника
    """

    name = models.CharField(
        verbose_name="Название",
        max_length=150,
    )

    slug = models.SlugField(
        verbose_name="Slug",
        unique=True,
    )

    parent = models.ForeignKey(
        "self",
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )

    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="categories/",
        blank=True,
    )

    sort_order = models.PositiveIntegerField(
        verbose_name="Порядок сортировки",
        default=0,
    )

    is_active = models.BooleanField(
        verbose_name="Активна",
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "catalog:category",
            kwargs={"slug": self.slug},
        )