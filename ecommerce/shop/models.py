from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
 

class Order(models.Model):
    items = models.CharField(max_length=1000)
    total = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
