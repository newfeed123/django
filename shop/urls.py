from django.urls import path, include, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [

    path("", views.index, name="index"),

    re_path(r'^(?P<product_slug>[\w-]+)-a(?P<product_id>\d+)\.hmtl$', views.product, name='product'),

    path("them-vao-gio-hang.html", views.add_to_cart, name="add_to_cart"),

    path("cap-nhat-gio-hang.html", views.update_cart, name="update_cart"),

    path("thong-bao.html", views.success, name="success"),

    path("gio-hang.html", views.cart, name="cart"),
    
    path("thanh-toan.html", views.checkout, name="checkout"),

    path("shop.html", views.category, name="shop"),

    path("lien-he.html", views.contact, name="contact"),

    path("kiem-tra-don-hang.html", views.check_order, name="check_order"),
    
    path("<slug:category_slug>.html", views.category, name="category"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
