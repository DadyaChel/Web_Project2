from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО клиента')
    price = models.IntegerField(verbose_name='цена товара')

    class Meta:
        verbose_name = 'Товар'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО клиента')
    age = models.IntegerField(verbose_name='возраст клиента')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    date_purchase = models.DateField(verbose_name='Дата покупки')

    def __str__(self):
        return self.name
