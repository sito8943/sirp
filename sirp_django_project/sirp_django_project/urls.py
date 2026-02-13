"""
URL configuration for sirp_django_project.

This file intentionally keeps the default Django routing setup.
"""

from django.contrib import admin
from django.urls import include, path

from sirp_django_project.subscriptions.views import LandingPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", LandingPageView.as_view(), name="home"),
    path("", include("sirp_django_project.subscriptions.urls")),
]
