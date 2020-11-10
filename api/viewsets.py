# rest framework
from rest_framework.response import Response
from rest_framework.decorators import action

# base
from base.viewsets import ReadOnlyModelViewSet

# models
from sales.models import Sale

# serializers
from api.serializers import SaleSerializer


class SaleViewSet(ReadOnlyModelViewSet):
    model = Sale
    serializer_class = SaleSerializer

    def list(self, *args, **kwargs):
        return Response({
            'total_sales': self.get_queryset().count(),
            'months': self.model.get_data(),
        })

    @action(detail=False, methods=('post',), url_path='data')
    def get_data(self, request, pk=None):
        previous_sales_count = self.model.objects.count()
        self.model.create_sales_from_external_data()
        sales_count = self.model.objects.count()
        return Response({
            'need_reload': not previous_sales_count == sales_count
        })
