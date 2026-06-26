from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "sort_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "sort_order",
        "name",
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "article",
        "name",
        "category",
        "price",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "article",
        "name",
        "main_keyword",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "article",
    )