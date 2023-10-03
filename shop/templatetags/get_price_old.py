from django import template
from .format_currenct_vietnam import format_currenct_vietnam
register = template.Library()

@register.simple_tag
def get_price_old(price, price_sale):

    return format_currenct_vietnam(price) if price_sale else ""