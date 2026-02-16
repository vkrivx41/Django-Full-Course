from django_filters import FilterSet

from api.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['iexact', 'icontains'],
            'price': ['exact', 'gt', 'lt', 'range']
        }
