from rest_framework import serializers
from ..models import Vegetable


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = [
            'id',
            'name_ko',
            'name_en',
            'unit',
            'sub_unit',
            'sub_unit2',
        ]
        read_only_fields = [
            'id',
        ]
