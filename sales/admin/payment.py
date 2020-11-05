# django
from django.contrib import admin

# models
from sales.models import Payment

# base
from base.admin import BaseModelAdmin


@admin.register(Payment)
class PaymentAdmin(BaseModelAdmin):
    list_display = (
        'sale',
        'amount',
        'kind',
    )
