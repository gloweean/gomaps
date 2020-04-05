from django.contrib import admin
from user.models import User


@admin.register(User)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'username',
        'email',
        'name',
        'password',
        'gender',
        'birthday',
        'phone_num',
        'postal_code',
        'address',
        'date_joined',
        'is_staff',
    ]
    
    readonly_fields = [
        'username',
        'date_joined',
    ]
