#những vấn đề xử lý bên ngoài để hỗ trợ
import uuid
import os
import re
import locale, random, string

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    
    return os.path.join('shop/images/product/', filename)

def get_skip_slug_article(path):
    # argentina-giau-thanh-tich-nhat-lich-su-a11.hmtl
    # form url mới update: slug-a-id.html

    # last_path = path.split('/')[-1]
    skip_slug = None
    match = re.search(r'^(?P<article_slug>[\w-]+)-a\d+.html$', path)
    if match:
        skip_slug = match.group('article_slug')

    return skip_slug

def format_currenct_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')
    #300000 -> 300.000

    formatted_number = locale.format_string("%d", number, grouping=True) + " đ" #grouping=True có phân tách
    return formatted_number

def chunked(items, quantity_per_group):
    result = []

    for i in range(0, len(items), quantity_per_group):
        chunk = items[i : i+quantity_per_group]
        #quantity_per_group : bước nhảy, vd quantity_per_group = 3 => lấy các phần tủ từ i -> i+3
        result.append(chunk)

    return result

def generate_order_code(length):
    #tao code random
    letters = string.ascii_uppercase + string.digits

    return ''.join(random.choice(letters) for _ in range(length))
