from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .define import *
from .models import *
from .helpers import *
from .forms import *
from .send_mail import *
import re
# Create your views here.

def index(request):
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by('ordering')

    for category in items_category:
        #đặt cho category 1 thuộc tính mới
        category.product_filter = category.product_set.filter(status=APP_VALUE_STATUS_ACTIVE, special = True).order_by('ordering')[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    items_product_latest = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('-id')[:SETTING_PRODUCT_TOTAL_ITEMS_LATEST_INDEX]

    items_product_latest = chunked(items_product_latest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLICE)

    # print("test....", items_product_latest)

    items_product_hot = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('-total_sold')[:SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX]

    items_product_hot = chunked(items_product_hot, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLICE)

    items_product_random = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('?')[:SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX]

    items_product_random = chunked(items_product_random, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLICE)
    

    # print("tesst .............", items_category)
    return render(request, APP_PATH_PAGES + 'index.html', {
        'title_page': "Trang chủ",
        # 'items_article_special': items_article_special,
        'items_category': items_category,
        'items_product_latest': items_product_latest,
        'items_product_hot': items_product_hot,
        'items_product_random': items_product_random,
    })

def product(request, product_slug, product_id):
    item_product = get_object_or_404(Product, id=product_id, slug=product_slug, status=APP_VALUE_STATUS_ACTIVE)

    items_product_related = Product.objects.filter(category=item_product.category, status=APP_VALUE_STATUS_ACTIVE).order_by('-id').exclude(id=product_id)[:SETTING_PRODUCT_TOTAL_ITEMS_RELATED] 

    return render(request, APP_PATH_PAGES + 'detail.html', {
        'title_page': item_product.name,
        'item_product': item_product,
        'items_product_related': items_product_related,
    })

def category(request, category_slug="shop"):
    item_category = None

    if category_slug != 'shop':
        item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)

    items_product = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('-id') #filter ra cac product co status = APP_VALUE_STATUS_ACTIVE

    #tao 1 dict
    params = {
        'order': request.GET.get('order') if request.GET.get('order') == 'price' else '-price',
        'minPrice': request.GET.get('minPrice', ''), #'': nếu ko có minPrice do user nhập thì mặc định để rỗng
        'maxPrice': request.GET.get('maxPrice', ''),
        'planting': request.GET.get('planting', ''),
        'keyword': request.GET.get('keyword', '')
    }

    items_product = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by(params['order'] + '_real') 

    items_planting_methods = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by(params['order'] + '_real') 

    if item_category:
        items_product = items_product.filter(category=item_category) #filter product theo item category

    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('ordering')[:SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR]

    if params['minPrice']: 
        items_product = items_product.filter(price_real__gte=params['minPrice']) #filter product theo price_real 

    if params['maxPrice']: 
        items_product = items_product.filter(price_real__lte=params['maxPrice']) #filter product theo price_real 

    if params['planting']: 
        items_product = items_product.filter(planting_methods__id=params['planting']) #filer product theo id cua planting_methods

    if params['keyword']: 
        items_product = items_product.filter(name__iregex=re.escape(params['keyword']))

    items_planting_methods = PlantingMethod.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('ordering')[:SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR] 

    product_count = items_product.count()

    paginator = Paginator(items_product, 3)
    page = request.GET.get('page')
    items_product = paginator.get_page(page)

    items_product_latest = Product.objects.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('-id')[:SETTING_PRODUCT_TOTAL_ITEMS_LATEST_SIDEBAR]

    items_product_latest = chunked(items_product_latest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLICE)


    return render(request, APP_PATH_PAGES + 'category.html', {
        'title_page': item_category.name if item_category else "CỬA HÀNG",
        'item_category': item_category,
        'items_category': items_category,
        'items_product': items_product,
        'params': params,
        'items_planting_methods': items_planting_methods,
        'paginator': paginator,
        'items_product_latest': items_product_latest,
        'product_count': product_count,
        
    })

def cart(request):
    items_product_cart = []
    total_price = 0

    #cart = {"2": 3, "10": 2}
    # 

    if 'cart' in request.session:
        cart = request.session['cart']

        # print(cart.items()) #[('18', 2), ('15', 3), ('13', 3), ('4', 2)]
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id) #lay sp theo product_id trong cart cua user
            item_price = product.price_real * quantity # thanh tien cua 1 product trong cart
            total_price += item_price

            cart_item = {
                'id': product_id, 
                'product': product,
                'quantity': quantity,
                'item_price': item_price,
            }

            items_product_cart.append(cart_item)

    return render(request, APP_PATH_PAGES + 'cart.html', {
        'title_page': "Giỏ hàng",
        'items_product_cart': items_product_cart,
        'total_price': total_price,
    })

def checkout(request):  
    # lấy dữ liệu từ trong session ra
    cart = request.session.get('cart', {})
    form = CheckoutForm()

    if not cart:
        absolute_url = request.build_absolute_uri(reverse('shop:cart'))
        return redirect(absolute_url) #chuyển hướng đến trang gio-hang.html


    if request.method == 'POST':
        form = CheckoutForm(request.POST) #validate form

        if form.is_valid():
            return checkout_post(request, form, cart)
        
    items_product_checkout = []
    total_order = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id) #lay sp theo product_id trong cart cua user
        name = product.name
        total = product.price_real * quantity
        total_order += total
        items_product_checkout.append({'name': name, 'total': total, 'quantity': quantity})

    return render(request, APP_PATH_PAGES + 'checkout.html', {
        'title_page': "Thanh Toán Đơn Hàng",
        'items_product_checkout': items_product_checkout,
        'total_order': total_order, 
        'form': form,
    })

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')

        if 'cart' not in request.session:#nếu là lần đầu đặt hàng
            request.session['cart'] = {}

        cart = request.session['cart']

        if product_id in cart:
            cart[product_id] += int(quantity) #neu product đó đã tồn tại trong cart thì cộng thêm
        else:
            cart[product_id] = int(quantity)

        request.session.modified = True #đánh dấu session đã bị thay đổi

        # print(cart) # {'id': quantity, }

    absolute_url = request.build_absolute_uri(reverse('shop:cart')) #app_name: shop , path_name: cart
    return redirect(absolute_url) #chuyển hướng đến trang gio-hang.html

def update_cart(request):
    # /cap-nhat-gio-hang.html?productId=37&action=decrease
    action = request.GET.get('action')
    product_id = request.GET.get('productId')
    product_id = str(product_id)

    cart = request.session.get('cart', {}) #nếu ko có thì cart có mặc định là {}

    if product_id in cart:
        if action == 'decrease':
            if cart[product_id] > 1:
                cart[product_id] -= 1
            else:
                del cart[product_id]
        elif action == "increase":
            cart[product_id] += 1
        elif action == "delete":
            del cart[product_id]

    request.session['cart'] = cart #gan lai cho cart trongs sesssion

    absolute_url = request.build_absolute_uri(reverse('shop:cart')) #app_name: shop , path_name: cart
    return redirect(absolute_url) #chuyển hướng đến trang gio-hang.html

def success(request):
    notify = NOTIFY_ORDER_SUCCESS
    
    if request.GET.get('t') == 'contact':
        notify = NOTIFY_CONTACT_SUCCESS

    return render(request, APP_PATH_PAGES + 'success.html', {
        'title_page': "Thông Báo",
        'notify': notify,
    })

def checkout_post(request, form, cart):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone']
    address = form.cleaned_data['address']

    code = generate_order_code(8)

    order = Order.objects.create(code=code, name=name, email=email, phone=phone, address=address) #tao 1 object de luu
    # print("data ok !!!")

    total_order = 0
    quantity_order = 0
    #lay id va quantity luu trong session

    items_order_mail = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        price = product.price_real
        total = price * quantity

        OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price, total=total)

        total_order += total
        quantity_order += quantity

        items_order_mail.append({'product': product.name, 'quantity': quantity, 'price': format_currenct_vietnam(price), 'total': format_currenct_vietnam(total)})
    
    order.total = total_order
    order.quantity = quantity_order
    order.save()

    del request.session['cart']

    link_order_check = request.build_absolute_uri(reverse('shop:check_order'))
    mail_content = mail_content_order(code, name, email, phone, address, total_order, items_order_mail, link_order_check)
    send_mail(NOTIFY_EMAIL_SUBJECT_CONTACT, mail_content, [email], [ADMIN_EMAIL_RECEIVE])

    absolute_url = request.build_absolute_uri(reverse('shop:success')) + '?t=order'

    return redirect(absolute_url) #chuyển hướng đến trang gio-hang.html


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return contact_post(request, form)
    return render(request, APP_PATH_PAGES + 'contact.html', {
        'title_page': "Liên Hệ",
        'form': form,
    })

def contact_post(request, form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone']
    message = form.cleaned_data['message']

    contacted = False

    Contact.objects.create(name=name, email=email, phone=phone, message=message, contacted=contacted)

    mail_content = mail_content_contact(name, email, phone, message)

    send_mail(NOTIFY_EMAIL_SUBJECT_CONTACT, mail_content, [email], email_bcc=[ADMIN_EMAIL_RECEIVE])

    absolute_url = request.build_absolute_uri(reverse('shop:success')) + '?t=contact'

    return redirect(absolute_url) #chuyển hướng đến trang gio-hang.html

def check_order(request):

    if request.method == "POST":
        return check_order_post(request)

    return render(request, APP_PATH_PAGES + 'check-order.html', {
        'title_page': "Kiểm tra đơn hàng",
        
    })

def check_order_post(request):
    order_code = request.POST.get('code', '')
    error_message = None
    item_order = None

    order_code = order_code.strip() #cat khoang trang du thua
    
    if order_code == '':
        error_message = NOTIFY_ORDER_CHECK_NOT_NULL
    else: 
        try:
            item_order = Order.objects.get(code=order_code)
        except Order.DoesNotExist:
            error_message = NOTIFY_ORDER_CHECK_NOT_EXIST

    return render(request, APP_PATH_PAGES + 'check-order.html', {
        'title_page': "Kiểm tra đơn hàng",
        'order_code': order_code,
        'error_message': error_message,
        'item_order': item_order,
    })