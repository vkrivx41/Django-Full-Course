from django_filters import FilterSet, DateFilter

from api.models import Product, Order


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['iexact', 'icontains'],
            'price': ['exact', 'gt', 'lt', 'range']
        }


class OrderFilter(FilterSet):
    created_at = DateFilter(field_name='created_at__date')  # extract the date portion

    class Meta:
        model = Order
        fields = {
            'status': ['iexact'],
            'created_at': ['lt', 'gt', 'exact']
        }
        