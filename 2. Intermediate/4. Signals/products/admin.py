from django.contrib import admin

from products.models import Seller, Product, Buyer, Order, ProductBackUp

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Order)
admin.site.register(ProductBackUp)
