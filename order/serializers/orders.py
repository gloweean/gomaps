from rest_framework import serializers
from ..models import Order
from customer.models import Customer
from user.serializers.user import UserSerializer
from vegetable.serializers.vegetables import VegetableSerializer

__all__ = [
    'OrderSerializer',
]


class CustomerOrderVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['operator']
        

class OrderSerializer(serializers.ModelSerializer):
    operator = UserSerializer(read_only=True)
    customer = CustomerOrderVersionSerializer(read_only=True)
    vegetable_name = VegetableSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id',
            'operator',
            'customer',
            'which_day',
            'vegetable_name',
            'order_quantity',
            'order_unit',
            'deliver_date',
            'order_status',
            'create_at',
            'update_at',
        ]
        read_only_fields = [
            'id',
            'create_at',
            'update_at',
        ]
