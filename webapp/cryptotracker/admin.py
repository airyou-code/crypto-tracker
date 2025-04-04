from django.contrib import admin
from .models import Cryptocurrency

# Register your models here.

@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'created_at', 'updated_at')
    search_fields = ('symbol', 'name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')