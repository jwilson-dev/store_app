from django.contrib import admin
from django.urls import path

from .views import proceed

urlpatterns = [
    path('proceed/', proceed, name='proceed')
]
