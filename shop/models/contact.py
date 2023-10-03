from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from shop.custom_field import *
from shop.define import *

class Contact(models.Model):
    name                = models.CharField(max_length=100)
    email               = models.EmailField()
    phone               = models.CharField(max_length=20)
    message             = models.TextField()
    contacted           = CustomBooleanFieldContact()
    message_admin       = models.TextField(blank=True)
    created             = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = TABLE_CONTACT_SHOW

    def __str__(self):
        return self.name
