# django
from django.contrib import admin

# models
from sales.models import Table

# base
from base.admin import BaseModelAdmin


@admin.register(Table)
class TableAdmin(BaseModelAdmin):
    list_display = (
        'number',
    )
