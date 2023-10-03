from django.urls import path, include, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    #path("123", views.index123, name="index123"),

    # path("category/<slug:category_slug>", views.category, name="category"),
    #update slug: category/the-thao.html -> /the-thao.html
    path("<slug:category_slug>.html", views.category, name="category"),

    # path("article/<slug:article_slug>", views.article, name="article"),
    #article/messi-the-thao.html -> /messi-the-thao-a11.html
    re_path(r'^(?P<article_slug>[\w-]+)-a(?P<article_id>\d+)\.hmtl$', views.article, name='article'),

    # path("feed/<slug:feed_slug>", views.feed, name="feed"),
    #feed/vnexpress -> tin-tuc-tong-hop-vnexpress.html
    re_path(r'^tin-tuc-tong-hop-(?P<feed_slug>[\w-]+)\.html$', views.feed, name='feed'),

    path("search.html", views.search, name="search"),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),

    
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
