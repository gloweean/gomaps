from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    def __str__(self):
        return self.course_area + " " + self.customer_name
    
    customer_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='고객명')
    course_area = models.CharField(max_length=100, blank=True, null=True, verbose_name='코스지역명')
    address = models.CharField(max_length=254, blank=True, null=True, verbose_name='고객주소')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='연락처')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)