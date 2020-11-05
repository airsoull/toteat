# django
from django.contrib import admin

# models
from sales.models import Product

# base
from base.admin import BaseModelAdmin


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = (
        'name',
        'sale',
        'category',
        'price',
        'quantity',
    )
