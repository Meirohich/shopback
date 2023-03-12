from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL, null=True
    )

