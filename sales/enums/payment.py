# django
from django.utils.translation import ugettext_lazy as _


class KindEnum:
    CASH = 'CASH'
    CREDIT_CARD = 'CREDIT_CARD'
    DEBIT_CARD = 'DEBIT_CARD'

    CHOICES = (
        (CASH, _('Cash')),
        (CREDIT_CARD, _('Credit card')),
        (DEBIT_CARD, _('Debit card')),
    )
