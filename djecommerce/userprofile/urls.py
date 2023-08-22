from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

from .views import vendor_detail, signup, my_account


urlpatterns = [
    path('vendors/<int:pk>/', vendor_detail, name='vendor_detail'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('my-account/', my_account, name='my_account'),
]
