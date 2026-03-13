"""Admin configuration for vendor models."""

from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface configuration for Product."""

    list_display = ("name", "price", "quantity", "vendor", "created_date")
