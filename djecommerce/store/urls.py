from django.contrib import admin
from django.urls import path, include

from .views import product_detail

urlpatterns = [
    path('<slug:slug>/', product_detail, name='product_detail'),
]
