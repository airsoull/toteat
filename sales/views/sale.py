# base
from base.views import BaseListView

# models
from sales.models import Sale


class SaleListView(BaseListView):
    model = Sale
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.related_objects()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sales = context['paginator'].object_list

        context['sum_total'] = sales.aggregate_sum_total()
        context['sales'] = sales
        return context
