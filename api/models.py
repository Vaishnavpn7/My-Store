from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Products(models.Model):
    name = models.CharField(unique=True, max_length=50)
    price = models.PositiveIntegerField()
    discription = models.CharField(max_length=200)
    catagory = models.CharField(max_length=50)
    image = models.ImageField(null=True, upload_to='images')

    @property
    def avg_rating(self):
        rating = self.review_set.all().values_list('rating', flat=True)
        if rating:
            return sum(rating) / len(rating)
        else:
            return 0

    @property
    def review_count(self):
        reviews = self.review_set.all().values_list('rating', flat=True)
        return len(reviews)

    def __str__(self):
        return self.name


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    options = (

        ('order-placed', 'order-placed'),
        ('in-cart', 'in-cart'),
        ('cancelled', 'cancelled'),

    )

    status = models.CharField(max_length=200, choices=options, default='in-cart')


class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment


class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    options = (

        ('order-placed', 'order-placed'),
        ('dispatched', 'dispatched'),
        ('in-transit', 'in-transit'),
        ('cancelled', 'cancelled'),

    )

    status = models.CharField(max_length=200, choices=options, default='order-placed')
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)

# modelsname.objects.create(feildname=value1,feild2=value2....)
# Products.objects.create(name="samsung 12",price=25000,discription="mobile",catagory="electronics")

# FILTER
# Products.objects.filter(catagory="electronics")
# to view as list add flat=true
# Products.objects.all().exclude(catagory="cloacthing")
# qs=Products.objects .get(id=1)
# UPDATE
# Products.objects.filter(id=3).update(price=1800)
# LESS THAN
# Products.objects.filter(price__lt=3000)
# __lt=<
# __lte=<=

# LIST CATAGORY
# Products.objects.values_list('catagory')
