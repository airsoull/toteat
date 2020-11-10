# rest framework
from rest_framework import mixins
from rest_framework import viewsets


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    model = None

    def get_queryset(self):
        return self.model.objects.all()
