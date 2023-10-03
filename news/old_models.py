# from django.db import models
# from django.urls import reverse
# from tinymce.models import HTMLField
# from .helpers import * #import file helper vừa tạo
# from .custom_field import *
# from .define import *
# # Create your models here.
# class Category(models.Model):

#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     #is_homepage = models.BooleanField(default=False)
#     is_homepage = CustomBooleanField() #custom lại
#     layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
#     ordering = models.IntegerField(default=0)

#     class Meta:
#         verbose_name_plural = TABLE_CATEGORY_SHOW #custom lai ten model

#     def get_absolute_url(self):
#         return reverse("category", kwargs={"category_slug": self.slug})

#     def __str__(self):
#         return self.name
    

# def get_file_path(instance, filename):
#         #ten user upload la image.jpg
#         ext = filename.split('.')[-1]#lấy cái đuôi jpg
#         filename = "%s.%s" % (uuid.uuid4(), ext)#uuid sinh chuỗi ngẫu nhiên, ghép chuỗi đó với cái đuôi ext lấy ở trên
#         return os.path.join('news/images/article/', filename) 

# class Article(models.Model):
#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
#     ordering = models.IntegerField(default=0)
#     #special = models.BooleanField(default=False)
#     special = CustomBooleanField()#custom lại check is_special 
#     publish_date = models.DateTimeField()
#     content = HTMLField() #content phải lưu ở dạng html
#     #content = models.TextField()
#     image = models.ImageField(upload_to=get_file_path)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE) #mqh giữa bài viết và category, on_delele : là khi xóa danh mục thì bài viết cũng xóa theo

#     class Meta:
#         verbose_name_plural = TABLE_ARTICLE_SHOW #custom lai ten model

#     def get_absolute_url(self):
#         return reverse("article", kwargs={"article_slug": self.slug, 'article_id': self.id})
    
#     def __str__(self):
#         return self.name
    
# class Feed(models.Model):
#     STATUS_CHOICE = (
#         ('draft', 'Draft'),
#         ('published', 'Published')
#     )
#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Draft')
#     ordering = models.IntegerField(default=0)
#     link = models.CharField(max_length=250, )#luu link rss

#     class Meta:
#         verbose_name_plural = TABLE_FEED_SHOW #custom lai ten model

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse("feed", kwargs={"feed_slug": self.slug})

    
    

