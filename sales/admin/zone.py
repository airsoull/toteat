# django
from django.contrib import admin

# models
from sales.models import Zone

# base
from base.admin import BaseModelAdmin


@admin.register(Zone)
class ZoneAdmin(BaseModelAdmin):
    list_display = (
        'name',
    )
