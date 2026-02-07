from django.contrib import admin

from products.models import Seller, Product, Buyer, Order


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'seller')}

class SellerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer)
admin.site.register(Order)
