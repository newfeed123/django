#tạo file này để nếu muốn import nhiều models thì chỉ cần 1 dòng: from .models import Category
from .category import Category
from .product import Product
from .planting_method import PlantingMethod
from .order import Order
from .order_item import OrderItem
from .contact import Contact

__all__= ['Category', 'Product', 'PlantingMethod', 'Order', 'OrderItem', 'Contact']