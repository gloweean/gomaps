from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    DAY_CHOICE = (
        ('MON', '월'),
        ('TUE', '화'),
        ('WED', '수'),
        ('THU', '목'),
        ('FRI', '금'),
    )
    customer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='고객명')
    course_area = models.CharField(max_length=100, blank=True, null=True, verbose_name='코스지역명')
    which_day = models.CharField(max_length=10, choices=DAY_CHOICE, default='코스요일',)
    address = models.CharField(max_length=254, blank=True, null=True, verbose_name='고객주소')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='연락처')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)