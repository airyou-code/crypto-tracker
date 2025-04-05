from django.contrib import admin
from .models import Cryptocurrency
from django.db import models
from core.widgets import JSONEditorWidget

# Register your models here.

@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'created_at', 'updated_at')
    search_fields = ('symbol', 'name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    formfield_overrides = {
        models.JSONField: {
            "widget": JSONEditorWidget(
                attrs={"style": "margin-bottom:30px;height:350px;width:100%;"}
            )
        },
    }
