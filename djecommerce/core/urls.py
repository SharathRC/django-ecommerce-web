from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView
)

from .views import item_list


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('items/', item_list, name='item_list'),
]