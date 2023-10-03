from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from shop.helpers import *
from shop.custom_field import *
from shop.define import *
from .category import Category
from .planting_method import PlantingMethod

class Product(models.Model):
    name        = models.CharField(unique=True, max_length=100)
    slug        = models.SlugField(unique=True, max_length=100)
    status      = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering    = models.IntegerField(default=0)
    #special = models.BooleanField(default=False)
    special     = CustomBooleanField()#custom lại check is_special 
    price       = models.DecimalField(max_digits=10, decimal_places=0)
    price_sale  = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True) #có thể có hoặc không
    price_real  = models.DecimalField(max_digits=10, decimal_places=0, editable=False) # dùng price_real để sắp xếp giá do ko thể sx theo price (nếu price_sale có thì sẽ sai)
    total_sold  = models.IntegerField(default=0, editable=False) 
    summary     = models.TextField()
    content     = HTMLField() #content phải lưu ở dạng html
    #content = models.TextField()
    image = models.ImageField(upload_to=get_file_path)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE) #mqh giữa bài viết và category, on_delele : là khi xóa danh mục thì bài viết cũng xóa theo
    planting_methods = models.ManyToManyField(PlantingMethod) #mqh n-n

    class Meta:
        verbose_name_plural = TABLE_PRODUCT_SHOW #custom lai ten model

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"product_slug": self.slug, 'product_id': self.id})
    
    #định nghĩa lại phương thức save
    def save(self, *args, **kwargs):
        if self.price_sale:
            self.price_real = self.price_sale
        else:
            self.price_real = self.price

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
