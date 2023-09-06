from django.contrib import admin
from django.urls import path, include

from .views import homepage, about

urlpatterns = [
    path("", homepage, name="homepage"),
    path("about/", about, name="about"),
]
