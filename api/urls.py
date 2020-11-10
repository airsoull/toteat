# django
from django.urls import path
from django.urls import include

# rest framework
from rest_framework import routers

# viewsets
from api import viewsets

router = routers.DefaultRouter()
router.register(r'sales', viewsets.SaleViewSet, 'sale')

urlpatterns = [
    path('', include(router.urls)),
]
