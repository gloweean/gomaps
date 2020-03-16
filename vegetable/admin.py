from django.contrib import admin
from vegetable.models import Vegetable

@admin.register(Vegetable)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'name_ko',
        'name_en',
        'unit',
        'sub_unit',
        'sub_unit2',
    ]
    
    readonly_fields = [
    ]
