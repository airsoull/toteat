# django
from django.db import models
from django.db.models import Sum

# base
from base.managers import QuerySet


class SaleQuerySet(QuerySet):

    def related_objects(self):
        queryset = super().related_objects()
        return queryset

    def aggregate_sum_total(self):
        return self.aggregate(sum_total=models.Sum('total'))['sum_total']

    def total_by_months(self) -> list:
        return (
            self.model.objects.values('date_opened__month')
            .annotate(total_by_month=Sum('total'))
            .order_by('total_by_month')
        )
