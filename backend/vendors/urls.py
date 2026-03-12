"""URL configuration for vendor APIs."""

from django.urls import path

from .views import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
]
