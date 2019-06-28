from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pos.urls')),
    path('checkout/', include('checkout.urls')),
    path('admin/', admin.site.urls),
]
