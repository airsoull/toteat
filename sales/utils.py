# django
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


# models
from sales.models import Zone
from sales.models import Table
from sales.models import Category

# enums
from sales.enums.payment import KindEnum

zones = {}
tables = {}
categories = {}


def get_zone(zone_name: str) -> Zone:
    if zone_name not in zones:
        zones[zone_name] = (
            Zone.objects.get_or_create(name=zone_name)[0]
        )
    return zones[zone_name]


def get_category(category_name: str) -> Category:
    if category_name not in categories:
        categories[category_name] = (
            Category.objects.get_or_create(name=category_name)[0]
        )
    return categories[category_name]


def get_table(table_number: int) -> Table:
    if table_number not in tables:
        tables[table_number] = (
            Table.objects.get_or_create(number=table_number)[0]
        )
    return tables[table_number]


def str_to_datetime(string_datetime: str) -> timezone.datetime:
    time_zone = timezone.get_current_timezone()
    return timezone.make_aware(
        timezone.datetime.strptime(string_datetime, '%Y-%m-%d %H:%M:%S'),
        time_zone,
    )


def get_sale_reference() -> dict:
    return {
        'date_closed': str_to_datetime,
        'waiter': 'waiter',
        'cashier': 'cashier',
        'diners': 'diners',
        'date_opened': str_to_datetime,
        'table': get_table,
        'total': 'total',
        'id': 'external_id',
        'zone': get_zone,
    }


def payment_type_to_internal_kind(kind):
    data = {
        'Efectivo': KindEnum.CASH,
        'Tarjeta crédito': KindEnum.CREDIT_CARD,
        'Tarjeta débito': KindEnum.DEBIT_CARD,
    }
    return data[kind]


def get_payment_reference() -> dict:
    return {
        'amount': 'amount',
        'type': payment_type_to_internal_kind,
    }


def get_product_reference() -> dict:
    return {
        'name': 'name',
        'category': get_category,
        'price': 'price',
        'quantity': 'quantity',
    }


def get_key_and_value_from_reference(reference, key_data, value_data):
    if callable(reference[key_data]):
        value = reference[key_data](value_data)
        key = key_data
    else:
        value = value_data
        key = reference[key_data]

    return key, value


def get_months() -> dict:
    return {
        1: _('january'),
        2: _('february'),
        3: _('march'),
        4: _('april'),
        5: _('may'),
        6: _('june'),
        7: _('july'),
        8: _('august'),
        9: _('september'),
        10: _('october'),
        11: _('november'),
        12: _('december'),
    }
