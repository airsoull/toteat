# django
from django.contrib import admin

# models
from sales.models import Sale

# base
from base.admin import BaseModelAdmin


@admin.register(Sale)
class SaleAdmin(BaseModelAdmin):
    list_display = (
        'external_id',
        'table',
        'zone',
        'total',
        'created_at',
    )
    list_filter = (
        'zone',
    )
