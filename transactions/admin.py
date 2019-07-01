from django.contrib import admin

from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','ref_code','trans_date')
    list_display_links = ('ref_code', 'id')
    search_fields = ('ref_code',)
    readonly_fields = ('items', 'trans_date')

admin.site.register(Transaction, TransactionAdmin)
