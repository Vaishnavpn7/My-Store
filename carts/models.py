from django.db import models


class Carts(models.Model):
    products = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.products
