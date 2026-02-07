from django.contrib import admin

from products.models import Seller, Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'seller')}

class SellerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
