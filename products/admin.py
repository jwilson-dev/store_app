from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'stock', 'price', 'add_date', 'last_restock')
    list_display_links = ('code', 'name')
    list_filter = ('category',)
    search_fields = ('code', 'name')
    list_editable = ('stock',)
    readonly_fields = ('add_date','last_restock')

admin.site.register(Product, ProductAdmin)
