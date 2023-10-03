APP_VALUE_STATUS_ACTIVE = 'published'
APP_VALUE_LAYOUT_DEFAULT = 'list'
APP_VALUE_STATUS_DEFAULT = 'Draft'
APP_PATH_PAGES = 'pages/'
APP_VALUE_IMAGE_DEFAULT = '/media/news/images/feed/no-image.png'
APP_VALUE_STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
APP_VALUE_LAYOUT_CHOICES = (
        ('list', 'List'),
        ('gird', 'Grid')
    )

SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL = 5
SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE = 2
SETTING_ARTICLE_TOTAL_ITEMS_RANDOM = 5
SETTING_ARTICLE_TOTAL_ITEMS_RECENT = 6

SETTING_PRICE_COIN_TOTAL_ITEMS = 5
SETTING_PRICE_GOLD_TOTAL_ITEMS = 5

SETTING_FEED_TOTAL_ITEMS_SIDEBAR = 5

SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR = 5



SETTING_API_LINK_PRICE_COIN = 'http://apiforlearning.zendvn.com/api/get-coin'
SETTING_API_LINK_PRICE_GOLD = 'http://apiforlearning.zendvn.com/api/get-gold'


TABLE_CATEGORY_SHOW = 'Category'
TABLE_ARTICLE_SHOW = 'Article'
TABLE_FEED_SHOW = 'Feed'

ADMIN_SRC_JS = ('my_admin/js/general.js', 'my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js',)
ADMIN_SRC_CSS = {'all': ('my_admin/css/custom.css',) }
ADMIN_HEADER_NAME = "ZendVN Administration"