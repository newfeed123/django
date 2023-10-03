from django.db import models
from django.urls import reverse

from shop.custom_field import *
from shop.define import *

# Create your models here.
class Category(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    #is_homepage = models.BooleanField(default=False)
    is_homepage = CustomBooleanField() #custom lại
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW #custom lai ten model

    # def get_absolute_url(self):
    #     return reverse("shop_category", kwargs={"category_slug": self.slug}) #"shop_category" là tên path 
    
    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"category_slug": self.slug}) #bên urls của app shop khai báo app_name = 'shop'

    def __str__(self):
        return self.name
    

    


    


    
    

