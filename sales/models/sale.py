# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# base
from base.models import BaseModel

# services
from sales import services

# utils
from sales import utils

# models
from sales.models import Payment
from sales.models import Product


class Sale(BaseModel):
    external_id = models.CharField(
        _('external id'),
        max_length=255,
        unique=True,
    )
    date_closed = models.DateTimeField(
        _('date closed'),
    )
    zone = models.ForeignKey(
        'sales.Zone',
        verbose_name=_('zone'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='sales',
    )
    waiter = models.CharField(
        _('waiter'),
        max_length=255,
    )
    cashier = models.CharField(
        _('cashier'),
        max_length=255,
    )
    diners = models.PositiveSmallIntegerField(
        _('dinners'),
    )
    date_opened = models.DateTimeField(
        _('date opened'),
    )
    table = models.ForeignKey(
        'sales.Table',
        verbose_name=_('table'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='sales',
    )
    total = models.DecimalField(
        _('total'),
        max_digits=20,
        decimal_places=2,
    )

    class Meta:
        ordering = (
            'created_at',
        )

    def __str__(self):
        return self.external_id

    @classmethod
    def create_sales_from_external_data(cls):
        sales_data = services.get_sales_data()
        if not sales_data:
            return

        sale_reference = utils.get_sale_reference()
        sale_external_ids = cls.objects.values_list('external_id', flat=True)

        sales = []
        for sale_data in sales_data:
            if sale_data['id'] in sale_external_ids:
                continue

            data = {}
            for key_data, value_data in sale_data.items():
                if key_data not in sale_reference:
                    continue

                key, value = utils.get_key_and_value_from_reference(
                    sale_reference,
                    key_data,
                    value_data,
                )

                data[key] = value

            sales.append(
                cls(**data)
            )

        cls.objects.bulk_create(sales)

        Payment.create_payments_from_external_data(sales_data)
        Product.create_products_from_external_data(sales_data)
