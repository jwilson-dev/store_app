from django.contrib import admin
from django.urls import path

from .views import pos, search, add_to_cart, checkout
from checkout.views import proceed

urlpatterns = [
    path('', pos, name='index'),
    path('search/$', search, name='search' ),
    path('<int:products_id>', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', proceed, name='proceed'),
]
