from django.db import models
from django.contrib.auth import get_user_model
from customer.models import Customer
from vegetable.models import Vegetable

User = get_user_model()


class Order(models.Model):
    def __str__(self):
        return self.customer.course_area + ' ' + self.customer.customer_name + ' ' + self.which_day + ' ' + self.operator.name
    
    DAY_CHOICE = (
            ('MON', '월'),
            ('TUE', '화'),
            ('WED', '수'),
            ('THU', '목'),
            ('FRI', '금'),
        )
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    which_day = models.CharField(max_length=10, choices=DAY_CHOICE, default='코스요일',)
    vegetable_name = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='주문량')
    order_unit = models.CharField(max_length=100, blank=True, null=True, verbose_name='주문 단위')
    
    class Meta:
        verbose_name = '주문'
