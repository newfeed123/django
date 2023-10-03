from django import template

register = template.Library()

@register.simple_tag

def check_and_show_value(value):
    return value if value else ""