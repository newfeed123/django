from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from shop.custom_field import *
from shop.define import *

from .product import Product
from .order import Order

# Create your models here.
class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    total = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return ""


    

    


    


    
    

