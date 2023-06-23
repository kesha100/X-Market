from django.db import models

# Create your models here.


class Card(models.Model):
    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=3, max_digits=7, null=True)
    status = models.CharField(choices=CHOICES, max_length=20)