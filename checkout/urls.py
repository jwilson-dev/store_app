from django.contrib import admin
from django.urls import path

from .views import proceed

urlpatterns = [
    path('payment/', proceed, name='proceed')
]
