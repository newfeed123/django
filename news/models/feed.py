from django.db import models
from django.urls import reverse
from news.define import *

class Feed(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Draft')
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250, )#luu link rss

    class Meta:
        verbose_name_plural = TABLE_FEED_SHOW #custom lai ten model

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("feed", kwargs={"feed_slug": self.slug})