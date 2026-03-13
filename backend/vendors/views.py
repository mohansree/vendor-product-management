"""Views for vendor-related API endpoints."""

from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import RegisterSerializer, ProductSerializer


class RegisterView(generics.CreateAPIView):
    """API view for vendor registration."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for managing vendor products."""

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return products belonging to the logged-in vendor."""
        return Product.objects.filter(vendor=self.request.user)

    def perform_create(self, serializer):
        """Save product with logged-in vendor."""
        serializer.save(vendor=self.request.user)
