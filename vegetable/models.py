from django.db import models


class Vegetable(models.Model):
    def __str__(self):
        return self.name_ko
    
    name_ko = models.CharField(max_length=100, blank=True, null=True, verbose_name='야채 이름(한글)')
    name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name='야채 이름(영어)')
    unit = models.CharField(max_length=100, blank=True, null=True, verbose_name='주요 단위')
    sub_unit = models.CharField(max_length=100, blank=True, null=True, verbose_name='보조 단위')
    sub_unit2 = models.CharField(max_length=100, blank=True, null=True, verbose_name='보조 단위2')

