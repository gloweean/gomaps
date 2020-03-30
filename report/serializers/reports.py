from rest_framework import serializers
from ..models import TotalOrder
from vegetable.serializers.vegetables import VegetableSerializer


__all__ = [
    'TotalOrderSerializer',
]


class TotalOrderSerializer(serializers.ModelSerializer):
    vege_name = VegetableSerializer(read_only=True)
    
    class Meta:
        model = TotalOrder,
        fields = [
            'id',
            'deliver_date',
            'vege_name',
            'quantity_ctn',
            'quantity_bag',
            'quantity_kg',
            'quantity_ea',
            'memo',
            'create_at',
            'update_at',
        ]

        read_only_fields = [
            'id',
            'create_at',
            'update_at',
        ]