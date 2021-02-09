from django.contrib import admin
from Product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'description', 'price', 'height',
                    'width', 'length', 'weight')

admin.site.register(Product, ProductAdmin)
