from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
# from django.http import HttpResponse
from .models import Category, Article, Feed
from django.utils import timezone
import re
import feedparser
# import json
from bs4 import BeautifulSoup
from .define import *

# def index(request):
#     return HttpResponse("Hello, world. You're at the NEWS index 1234666.")

# def index123(request):
#     return HttpResponse("Hello, world. You 're at the NEWS index 12345666")

def index(request):
    items_article_special = Article.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by('ordering')

    for category in items_category:
        #đặt cho category 1 thuộc tính mới
        category.article_filter = category.article_set.filter(status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    return render(request, APP_PATH_PAGES + 'index.html', {
        'title_page': "Trang chủ",
        'items_article_special': items_article_special,
        'items_category': items_category,
    })

def category(request, category_slug):
    #category_slug -> database -> article thuộc category đó -> đổ dữ liệu ra ngaoif client 
    item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)

    items_article = Article.objects.filter(category=item_category, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date') 

    paginator = Paginator(items_article, 2) #moi 1 page cho 2 bai viet

    # http://127.0.0.1:8000/the-thao.html?page=2
    page = request.GET.get('page')
    items_article = paginator.get_page(page)

    return render(request, APP_PATH_PAGES + 'category.html', {
        'title_page': item_category.name,
        "item_category": item_category,
        'items_article': items_article,
        'paginator': paginator,
    })

def article(request, article_slug, article_id):
    item_article = get_object_or_404(Article, id=article_id, slug=article_slug, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now())

    #article lien quan: exclude() loai bỏ article có slug giống với article hiện tại
    items_article_related = Article.objects.filter(category=item_article.category, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date').exclude(slug=article_slug)[:SETTING_ARTICLE_TOTAL_ITEMS_RECENT] 

    return render(request, APP_PATH_PAGES + 'article.html', {
        'title_page': item_article.name,
        'item_article': item_article,
        'items_article_related': items_article_related,
    })

def feed(request, feed_slug):
    item_feed = get_object_or_404(Feed, slug=feed_slug, status=APP_VALUE_STATUS_ACTIVE)
    # print(item_feed.link)
    feed = feedparser.parse(item_feed.link) #chuyen tu .rss sang JSON

    #print(feed)
    # with open('feed.json', 'w', encoding='utf-8') as f:
    #     json.dump(feed, f, ensure_ascii=False)

    items_feed = []
    try:
        feed = feedparser.parse(item_feed.link) #chuyen tu .rss sang JSON
        for entry in feed.entries:
            soup = BeautifulSoup(entry.summary, 'html.parser')
            img_tag = soup.find('img')
            src_img = APP_VALUE_IMAGE_DEFAULT
            if img_tag:
                src_img = img_tag['src']

            item = {
                'title': entry.title,
                'link': entry.link,
                'pub_date': entry.published,
                'img': src_img,
            }
            items_feed.append(item)
    except:
        print("Get feed: Error !!!")

    return render(request, APP_PATH_PAGES + 'feed.html', {
        'title_page': "Tin tức tổng hợp " + item_feed.name,
        'items_feed': items_feed,
        'item_feed': item_feed,
    })

def search(request):
    keyword = request.GET.get('keyword')
    items_article = Article.objects.filter(name__iregex=re.escape(keyword), status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date') 

    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE) #moi 1 page cho 2 bai viet
    page = request.GET.get('page') #page ma usser muon toi
    items_article = paginator.get_page(page) #get toan bo phan tu trong page do

    # print(keyword)
    return render(request, APP_PATH_PAGES + 'search.html', {
        'title_page': "Tìm kiếm cho từ khóa" + keyword, 
        'items_article': items_article,
        'keyword': keyword,
        'paginator': paginator,
    })

def about(request):

    return render(request, APP_PATH_PAGES + 'about.html', {
        'title_page': "Giới Thiệu",
    })

def contact(request):

    return render(request, APP_PATH_PAGES + 'contact.html', {
        'title_page': "Liên Hệ",
    })

