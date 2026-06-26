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
        verbose_name="SEO-заголовок",
        max_length=255,
        blank=True,
    )

    meta_description = models.TextField(
        verbose_name="Meta-описание",
        blank=True,
    )

    main_keyword = models.CharField(
        verbose_name="Главный поисковый запрос",
        max_length=255,
        blank=True,
        help_text="Основной поисковый запрос."
    )

    search_aliases = models.TextField(
        verbose_name="Дополнительные поисковые запросы",
        blank=True,
        help_text="По одному запросу на строку.",
    )


    # ------------------------------------------------------------------
    # Marketing
    # ------------------------------------------------------------------

    competitive_advantages = models.TextField(
        verbose_name="Конкурентные преимущества",
        blank=True,
        help_text="Конкретные преимущества товара перед конкурентами.",
    )

    unique_selling_proposition = models.TextField(
        verbose_name="Уникальное торговое предложение (УТП)",
        blank=True,
        help_text="Главная идея продажи. Что получит покупатель после покупки.",
    )

    # ------------------------------------------------------------------
    # Service
    # ------------------------------------------------------------------

    is_active = models.BooleanField(
        verbose_name="Активен",
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["article"]


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "catalog:product",
            kwargs={"slug": self.slug},
        )

