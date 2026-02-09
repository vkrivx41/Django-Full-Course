from django.shortcuts import get_object_or_404
from django.db.models import Avg

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer, OrderSerializer, ProductsInfoSerializer
from api.models import Product, Order, OrderItem


@api_view(http_method_names=['GET'])
def product_list(request):
    products = Product.objects.prefetch_related(
        'orders', 'items'
    ).all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_detail(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)

    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def products_info(request):
    products = Product. Product.objects.prefetch_related('orders').all()
    serializer = ProductsInfoSerializer({
        'products': products,
        'count': products.count(),
        'avg_price': products.aggregate(avg=Avg('price'))['avg']
    })

    return Response(serializer.data)
