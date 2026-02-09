from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProductSerializer
from api.models import Product, Order, OrderItem


# @api_view(http_method_names=['GET', 'POST'])  # -> this would allow both GET and POST
@api_view(http_method_names=['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_detail(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
