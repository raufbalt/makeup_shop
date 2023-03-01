from django.db import models


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
    availability = models.PositiveSmallIntegerField(choices=Availability.choice)


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                             related_name='images')

    @staticmethod
    def generate_name():
        from random import randint
        return 'image' + str(randint(100000, 1000000))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(ProductImages, self).save(*args, **kwargs)