from django.contrib import admin
from django.urls import path, include

from .views import product_detail, category_detail, search, add_to_cart

urlpatterns = [
    path("search/", search, name="search"),
    path("add-to-cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("<slug:category_slug>/<slug:slug>/", product_detail, name="product_detail"),
    path("<slug:slug>/", category_detail, name="category_detail"),
]
