from django.contrib import admin

from core.models import Restaurant, Rating, Sale, Product, Order


admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)