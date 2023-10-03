from django.db import models
from django.urls import reverse

from shop.custom_field import *
from shop.define import *

# Create your models here.
class PlantingMethod(models.Model):

    name = models.CharField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = TABLE_PLANTING_METHOD_SHOW #custom lai ten model

    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.name
    

    


    


    
    

