from django.contrib import admin
from django.urls import path, include

from .views import (
    product_detail,
    category_detail,
    search,
    add_to_cart,
    cart_view,
    remove_from_cart,
    change_quantity,
    checkout,
    invalid_checkout,
    checkout_success,
)

urlpatterns = [
    path("search/", search, name="search"),
    path("add-to-cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path(
        "remove-from-cart/<str:product_id>", remove_from_cart, name="remove_from_cart"
    ),
    path("change-quantity/<int:product_id>/", change_quantity, name="change_quantity"),
    path("cart/", cart_view, name="cart_view"),
    path("cart/success/", checkout_success, name="success"),
    path("cart/checkout/", checkout, name="checkout"),
    path("cart/invalid-checkout/", invalid_checkout, name="invalid_checkout"),
    path("<slug:category_slug>/<slug:slug>/", product_detail, name="product_detail"),
    path("<slug:slug>/", category_detail, name="category_detail"),
]
