from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=2000, blank=False)
    quantity = models.PositiveSmallIntegerField(blank=True, default=1)
    price = models.PositiveIntegerField(default=0)

    #User
    phone_number = models.CharField(max_length=30,blank=False)
    address = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    inform = models.CharField(max_length=300, blank=True, default='Комментарий отсутствует')




