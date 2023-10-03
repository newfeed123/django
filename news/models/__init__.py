#tạo file này để nếu muốn import nhiều models thì chỉ cần 1 dòng: from .models import Category, Feed, Article
from .category import Category
from .article import Article
from .feed import Feed

__all__= ['Category', 'Article', 'Feed']