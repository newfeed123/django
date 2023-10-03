import re
from django import template
from django.utils.html import mark_safe

register = template.Library()

def highlight_shop(value, keyword):
    #value: ten product
    #keywords: tu khoa cua user

    if keyword == '':
        return value
    else:
        regex = re.compile(re.escape(keyword), re.IGNORECASE)

        return mark_safe(regex.sub(f'<span class="highlight">{keyword}</span>', value))
    #sub(1, 2) thay the 1 cho 2

register.filter('highlight_shop', highlight_shop)
