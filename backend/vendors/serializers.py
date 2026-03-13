"""Serializers for vendor-related API."""

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for vendor registration."""

    class Meta:
        """Metadata for the RegisterSerializer."""

        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Create a new user with hashed password."""
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        """Meta configuration for ProductSerializer."""

        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "quantity",
            "created_date",
        ]
        read_only_fields = ["id", "created_date"]
