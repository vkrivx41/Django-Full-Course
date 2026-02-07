from django.contrib import admin

from products.models import Seller, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'seller')}


admin.site.register(Seller)
admin.site.register(Product, ProductAdmin)
