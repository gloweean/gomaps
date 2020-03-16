from django.contrib import admin
from user.models import User


@admin.register(User)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'email',
        'name',
        'gender',
        'birthday',
        'phone_num',
        'postal_code',
        'address',
        'is_staff',
    ]
    
    readonly_fields = [
        'date_joined',
    ]
