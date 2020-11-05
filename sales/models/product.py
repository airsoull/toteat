# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# base
from base.models import BaseModel

from sales import utils


class Product(BaseModel):
    sale = models.ForeignKey(
        'sales.Sale',
        verbose_name=_('sale'),
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(
        _('name'),
        max_length=255,
    )
    category = models.ForeignKey(
        'sales.Category',
        verbose_name=_('category'),
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
    )
    price = models.DecimalField(
        _('price'),
        max_digits=20,
        decimal_places=2,
    )
    quantity = models.PositiveSmallIntegerField(
        _('quantity'),
    )

    class Meta:
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name

    @classmethod
    def create_products_from_external_data(cls, data: dict):
        Sale = cls.sale.field.related_model
        sales = Sale.objects.in_bulk(field_name='external_id')
        products_reference = utils.get_product_reference()

        products = []
        for sale_data in data:
            data = {
                'sale': sales[sale_data['id']]
            }

            for payment in sale_data['products']:
                for key_data, value_data in payment.items():
                    key, value = utils.get_key_and_value_from_reference(
                        products_reference,
                        key_data,
                        value_data,
                    )
                    data[key] = value

            products.append(
                cls(**data)
            )

        cls.objects.bulk_create(products)
