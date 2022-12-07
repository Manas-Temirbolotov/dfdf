from django.utils import timezone
from django.contrib import admin
from django.db import models
from django.urls import reverse_lazy


class Block(models.Model):
    number = models.IntegerField(verbose_name='Номер блока')
    price = models.IntegerField(verbose_name='Стоимость за квадратный метр квартиры')
    entrance = models.IntegerField(default=2, verbose_name='Количество подъездов')
    floor = models.IntegerField(verbose_name='Количество этажей', default=5)
    flat = models.IntegerField(verbose_name='Количество квартир на этаж', default=1)

    def __str__(self):
        return self.number


class Flat(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО владельца', null=True)
    date_sale = models.DateField(verbose_name='Дата продажи', default=timezone.now, null=True)
    status = models.CharField(max_length=20, choices=(
        ('ransom', 'Выкуп'),
        ('not complete', 'Выкуп не до конца'),
        ('terminated', 'Расторгнуто'),
        ('not sold', 'Не продано')
    ), verbose_name='Статус ')
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    area = models.FloatField(verbose_name= 'общая площадь')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('flat_detail', kwargs={'pk': self.id})
