from unicodedata import category
from django.contrib import admin

from .models import Order, Product

admin.site.site_header = "Django-Ecommerce"
admin.site.site_title = "hello"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
    search_fields = ['title', 'description']
    actions = ('change_category_to_default',)
    fields = ('title', 'price',)
    list_editable = ('price', 'category')

admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
