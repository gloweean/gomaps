from django.contrib import admin
from order.models import Order


@admin.register(Order)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'operator',
        'customer',
        'which_day',
        'vegetable_name',
        'order_quantity',
        'order_unit',
    ]
    
    readonly_fields = [
    ]