from django import template
from urllib.parse import urlencode 
register = template.Library()

@register.simple_tag
def query_to_string(params, query_add=None, value_add=None):
    # params = {
    #     'x': 'v',
    #     'y': 'g',
    #}
    #chuyển params từ 1 dict thành 1 dạng query string: => ?x=v&y=g

    params_obj = params.copy()
    if query_add and value_add:
        params_obj[query_add] = value_add

    params_obj = {k: v for k, v in params_obj.items() if v} #nhhững key nào trong params mà ko có value sẽ bị loại bỏ
    # http://127.0.0.1:8000/cay-canh-de-ban.html?order=price&minPrice=100000&maxPrice=700000&planting=1&page=2
    return urlencode(params_obj)