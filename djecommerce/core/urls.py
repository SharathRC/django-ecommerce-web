from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import homepage, about

urlpatterns = [
    path("", homepage, name="homepage"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("about/", about, name="about"),
]
