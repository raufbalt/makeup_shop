from django.db import models

class Category(models.Model):
    name_eng = models.CharField(max_length=30, blank=False)
    name_ru = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return f'{self.name_eng} / {self.name_ru}'
class Availability:
	have = 1
	have_not = 2
	choice = ((have, 'В наличии/available'), (have_not, 'Нет в наличии/not available'))


class Product(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Cosmetics', unique=True)
    preview = models.ImageField(upload_to='images/', null=True)
    desc_en = models.CharField(max_length=500, blank=True, default='No description yet.')
    desc_ru = models.CharField(max_length=500, blank=True, default='Нет описания.')
    price = models.PositiveIntegerField(blank=True, default=0)
    availability = models.PositiveSmallIntegerField(choices=Availability.choice, default='1')

    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
