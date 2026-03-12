"""Serializers for vendor-related API."""

from django.contrib.auth.models import User
from rest_framework import serializers


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
