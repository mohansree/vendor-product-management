"""Database models for the vendor product management system."""

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    """Model representing a product created by a vendor."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    vendor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self):
        """Return readable product name."""
        return self.name
