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
    
    STATUS_CHOICE = (
        ('ACCEPTED', '주문접수'),     # 작성 완료 시
        ('CLOSE', '주문마감'),        # 주문 마감 시간 이후 (수정 안됨)
        ('CONFIRMED', '관리자승인'),   # 관리자 확인
    )
    
    UNIT_CHOICE = (
        ('CTN', '박스'),
        ('BAG', '포'),
        ('KG', '키로'),
        ('EA', ''),
    )
    
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    which_day = models.CharField(max_length=10, choices=DAY_CHOICE, default='코스요일')
    vegetable_name = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    order_quantity = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='주문량')
    order_unit = models.CharField(max_length=100, choices=UNIT_CHOICE, default='CTN', verbose_name='주문 단위')
    
    deliver_date = models.DateField(blank=True, null=True)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='주문접수')
    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    class Meta:
        verbose_name = '주문'
