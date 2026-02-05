from django.db.models import Q, F

from products.models import Seller, Product


def run():
    products = Product.objects.all()
    print(products.values('slug'))