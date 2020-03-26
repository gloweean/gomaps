from rest_framework import serializers
from ..models import Customer
from user.serializers.user import UserSerializer

__all__ = [
    'CustomerSerializer',
]


class CustomerSerializer(serializers.ModelSerializer):
    operator = UserSerializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = [
            'id',
            'customer_name',
            'course_area',
            'address',
            'phone',
            'operator',
        ]
        read_only_fields = [
            'id',
        ]
