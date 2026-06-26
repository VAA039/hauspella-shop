from django.db import models
from django.urls import reverse

from .category import Category


class Product(models.Model):
    """
    Основная модель товара.

    Product является центральной сущностью платформы HAUSPELLA
    и используется как интернет-магазином, так и ERP.
    """


    # ------------------------------------------------------------------
    # Identity
    # ------------------------------------------------------------------

    article = models.CharField(
        verbose_name="Артикул",
        max_length=20,
        unique=True,
        help_text="Внутренний артикул HAUSPELLA (например: HSP-000001)"
    )

    name = models.CharField(
        verbose_name="Название",
        max_length=255,
    )

    slug = models.SlugField(
        verbose_name="Slug",
        unique=True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="products",
    )

    # ------------------------------------------------------------------
    # Commerce
    # ------------------------------------------------------------------

    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    old_price = models.DecimalField(
        verbose_name="Старая цена",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    # ------------------------------------------------------------------
    # Content
    # ------------------------------------------------------------------

    short_description = models.TextField(
        verbose_name="Краткое описание",
        blank=True,
    )

    description = models.TextField(
        verbose_name="Полное описание",
        blank=True,
    )


    # ------------------------------------------------------------------
    # SEO
    # ------------------------------------------------------------------

    seo_title = models.CharField(
        verbose_name="SEO Title",
        max_length=255,
        blank=True,
    )

    meta_description = models.TextField(
        verbose_name="Meta Description",
        blank=True,
    )

    main_keyword = models.CharField(
        verbose_name="Главный поисковый запрос",
        max_length=255,
        blank=True,
    )

    search_aliases = models.TextField(
        verbose_name="Дополнительные поисковые запросы",
        blank=True,
        help_text="По одному запросу на строку.",
    )