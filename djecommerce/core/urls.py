from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from .views import item_list

app_name = 'core'

urlpatterns = [
    path('items/', item_list, name='item_list'),
]