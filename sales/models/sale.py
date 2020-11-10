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

# managers
from sales.managers.sale import SaleQuerySet


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

    objects = SaleQuerySet.as_manager()

    class Meta:
        ordering = (
            'created_at',
        )

    def __str__(self):
        return self.external_id

    def get_months(self) -> list:
        return []

    @classmethod
    def get_data(cls) -> list:
        total_by_months = {
            d['date_opened__month']: d['total_by_month']
            for d in cls.objects.total_by_months()
        }

        data = []
        for key, month in sorted(utils.get_months().items()):
            month_data = {'month': month, 'value': 0}
            if key in total_by_months:
                month_data['value'] = total_by_months[key]

            data.append(
                month_data
            )
        return data

    @ classmethod
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

        if not sales:
            return

        cls.objects.bulk_create(sales)

        Payment.create_payments_from_external_data(sales_data)
        Product.create_products_from_external_data(sales_data)
