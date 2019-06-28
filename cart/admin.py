from django.contrib import admin

from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'ref_code', 'is_order', 'order_date', 'last_transaction' )
    readonly_fields = ('order_date', 'last_transaction')
admin.site.register(Cart, CartAdmin)
