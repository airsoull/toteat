# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# base
from base.models import BaseModel

# enums
from sales.enums.payment import KindEnum

# utils
from sales import utils


class Payment(BaseModel):
    sale = models.ForeignKey(
        'sales.Sale',
        verbose_name=_('sale'),
        on_delete=models.CASCADE,
        related_name='payments',
    )
    amount = models.DecimalField(
        _('amount'),
        max_digits=20,
        decimal_places=2
    )
    kind = models.CharField(
        _('kind'),
        max_length=50,
        choices=KindEnum.CHOICES,
    )

    class Meta:
        ordering = (
            'created_at',
        )

    def __str__(self):
        return self.kind

    @classmethod
    def create_payments_from_external_data(cls, data: dict):
        Sale = cls.sale.field.related_model
        sales = Sale.objects.in_bulk(field_name='external_id')
        payment_reference = utils.get_payment_reference()

        payments = []
        for sale_data in data:
            data = {
                'sale': sales[sale_data['id']]
            }

            for payment in sale_data['payments']:
                for key_data, value_data in payment.items():
                    key, value = utils.get_key_and_value_from_reference(
                        payment_reference,
                        key_data,
                        value_data,
                    )
                    if key == 'type':
                        # TODO: fix this!!!!
                        key = 'kind'
                    data[key] = value

            payments.append(
                cls(**data)
            )

        cls.objects.bulk_create(payments)
