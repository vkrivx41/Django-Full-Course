from django.db.models import Q, F

from products.models import Seller, Product


def run():
    sellers = Seller.objects.all()
    seller = sellers.first()
    print(sellers.values('phone'))