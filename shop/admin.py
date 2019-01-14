from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, CartItem, Cart

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)

