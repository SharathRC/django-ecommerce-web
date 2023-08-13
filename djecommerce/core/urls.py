from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView
)

from .views import (
    item_list,
    register,   
)


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', register, name='register'),
    
    path('items/', item_list, name='item_list'),
]