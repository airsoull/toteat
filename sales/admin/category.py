# django
from django.contrib import admin

# models
from sales.models import Category

# base
from base.admin import BaseModelAdmin


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = (
        'name',
    )
