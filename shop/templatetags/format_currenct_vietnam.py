
from django import template
import locale

register = template.Library()


def format_currenct_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')
    #300000 -> 300.000

    formatted_number = locale.format_string("%d", number, grouping=True) + " đ" #grouping=True có phân tách
    return formatted_number
register.filter('format_currenct_vietnam', format_currenct_vietnam)