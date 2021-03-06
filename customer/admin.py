from django.contrib import admin
from customer.models import Customer


@admin.register(Customer)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'customer_name',
        'course_area',
        'address',
        'phone',
        'operator',
    ]
    
    readonly_fields = [
    ]
