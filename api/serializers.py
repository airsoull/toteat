# rest framework
from rest_framework import serializers

# models
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    months = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'months',
            'data',
        )

    def get_months(self, obj):
        return []

    def get_data(self, obj):
        return []
