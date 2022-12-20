from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name', 'cat_is_active']
    prepopulated_fields = {'cat_slug': ('cat_name', )}
    list_editable = ['cat_is_active']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_name', 'pro_category', 'pro_price', 'pro_stock', 'pro_is_available', 'pro_is_active']
    prepopulated_fields = {'pro_slug': ('pro_name', )}
    list_editable = ['pro_price', 'pro_stock', 'pro_is_available', 'pro_is_active']


admin.site.register(Product, ProductAdmin)
