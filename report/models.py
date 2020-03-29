from django.db import models
from vegetable.models import Vegetable


class TotalOrder(models.Model):
    def __str__(self):
        return self.vege_name

    deliver_date = models.DateField(blank=True, null=True)
    vege_name = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity_ctn = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='CTN')
    quantity_bag = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='BAG')
    quantity_kg = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='KG')
    quantity_ea = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name='EA')
    memo = models.TextField(max_length=512, blank=True, null=True)

    create_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)
