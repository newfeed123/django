from django.forms.widgets import RadioSelect
from django.db import models

class CustomBooleanField(models.BooleanField):
    def formfield(self, **kwargs):
        kwargs['widget'] = RadioSelect(choices=((True, 'Có'), (False, 'Không'))) #đổi widget thành radio
        kwargs['initial'] = False

        return super().formfield(**kwargs)