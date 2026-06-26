from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, ProductImage



class ProductImageInline(admin.TabularInline):
    model = ProductImage

    readonly_fields = (
        "image_preview",
    )

    def image_preview(self, obj):
        if obj.pk and obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border-radius: 6px;" />',
                obj.image.url,
            )
        return "—"

    image_preview.short_description = "Предпросмотр"

    extra = 0

    fields = (
        "image_preview",
        "image_type",
        "sort_order",
        "image",
        "alt",
    )

    ordering = (
        "sort_order",
    )

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

    inlines = (
        ProductImageInline,
    )

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


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "image_type",
        "sort_order",
        "created_at",
    )

    list_filter = (
        "image_type",
    )

    search_fields = (
        "product__article",
        "product__name",
        "alt",
    )

    ordering = (
        "product",
        "sort_order",
    )