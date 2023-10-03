from django.contrib import admin
from django.http.request import HttpRequest
from .define import *
from .helpers import *
from django.utils.html import format_html
# Register your models here.


from .models import Category, Product, PlantingMethod, Order, OrderItem, Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'ordering')
    #prepopulated_fields = {'slug': ('name', )} #tự tạo slug, nhưng tiếng việt ko đúng
    
    list_filter = ["is_homepage", "status"]
    search_fields = ["name"]

    #sử dụng js trong admin.py
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class ProductAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'name', 'status', 'ordering', 'category', 'special', 'price_formatted', 'price_sale_formatted','get_planting_methods' ,'total_sold')
    #prepopulated_fields = {'slug': ('name', )} #tự tạo slug, nhưng tiếng việt ko đúng
    
    list_filter = ["status", "special", "planting_methods"]
    search_fields = ["name"]

    #sử dụng js trong admin.py
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    @admin.display(description="Planting Method")
    def get_planting_methods(self, obj):
        #obj là từng product trong bảng
        methods = [method.name for method in obj.planting_methods.all()]
        #obj.planting_methods.all() #lây hết ra các planting_method nếu product đó có nhiều
    
        return ', '.join(methods) #các phần tử trong list method sẽ join lại với nhau bằng , và chuyển thành dạng ' '
    
    #get_planting_methods.short_description = 'Planting Method' #đổi tên cách 1

    @admin.display(description="Price") #đổi lại tên cach 2
    def price_formatted(self, obj):
        return format_currenct_vietnam(obj.price)
    
    @admin.display(description="Price Sale")
    def price_sale_formatted(self, obj):
        return format_currenct_vietnam(obj.price_sale) if obj.price_sale else obj.price
    
    @admin.display(description="Image")
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

class PlantingMethodtAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    #prepopulated_fields = {'slug': ('name', )} #tự tạo slug, nhưng tiếng việt ko đúng
    
    list_filter = ["status"]
    search_fields = ["name"]

    #sử dụng js trong admin.py
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order', 'product', 'quantity', 'price', 'total', 'price_formatted', 'total_formatted')
    fields = ('order', 'product', 'quantity', 'price_formatted', 'total_formatted')
    
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False 
    @admin.display(description="Price")
    def price_formatted(self, obj):
        return format_currenct_vietnam(obj.price)
    
    @admin.display(description='Total')
    def total_formatted(self, obj):
        return format_currenct_vietnam(obj.total)

    
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('code', 'name', 'email', 'phone', 'created', 'quantity', 'total_formatted', 'address', 'total')
    fields = ('status', 'code', 'name', 'email', 'phone', 'created', 'quantity', 'total_formatted', 'address')
    list_display = ('code', 'name', 'email', 'phone', 'created', 'quantity', 'total_formatted', 'status')
    list_filter = ['status']
    search_fields = ['name']
    list_editable = ['status']

    inlines = [OrderItemInline]

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    def has_add_permission(self, request):
        return False
    
    @admin.display(description='Total')
    def total_formatted(self, obj):
        return format_currenct_vietnam(obj.total)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.status == 'finish':
            obj.update_total_sold()

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'message', 'created')
    fields          = ('name', 'email', 'phone', 'created', 'contacted', 'message', 'message_admin')
    list_display    = ('name', 'email', 'phone', 'created', 'contacted', 'message', 'message_admin')
    # prepopulated_fields = {'slug': ('name',)}
    list_filter     = ["contacted"]
    search_fields   = ["name"]

    class Media:
        js  = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PlantingMethod, PlantingMethodtAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)

admin.site.site_header=ADMIN_HEADER_NAME #custom lai ten trang Admin
