from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from .views import (
    vendor_detail,
    signup,
    my_account,
    my_store,
    product_form,
    edit_product,
    delete_product,
)


urlpatterns = [
    path("vendors/<int:pk>/", vendor_detail, name="vendor_detail"),
    path("signup/", signup, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("my-account/", my_account, name="my_account"),
    path("my-store/", my_store, name="my_store"),
    path("my-store/product-form/", product_form, name="product_form"),
    path("my-store/edit-product/<int:pk>/", edit_product, name="edit_product"),
    path("my-store/delete-product/<int:pk>/", delete_product, name="delete_product"),
]
