# Generated by Django 3.0.4 on 2020-03-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200326_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_unit',
            field=models.CharField(choices=[('CTN', '박스'), ('BAG', '포'), ('KG', '키로'), ('EA', '')], default='CTN', max_length=100, verbose_name='주문 단위'),
        ),
    ]
