from django.db.models import Avg

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import ProductSerializer, OrderSerializer, ProductsInfoSerializer
from api.models import Product, Order, OrderItem


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.prefetch_related(
        'orders', 'items'
    ).all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.prefetch_related('orders')
    serializer_class = ProductSerializer

    # lookup_field = 'id'  # the field name to lookup for products/<int:id>
    # lookup_field = 'name'  # the field name to lookup for products/<str:name>

    lookup_url_kwarg = 'product_id'  # the name of the dynamic url lookup products/<int:product_id>


class OrderListApiView(ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer


class UserOrderListApiView(ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Overwrite the queryset to filter only the orders belonging to the logged in user
        :param self: refers back to the API view, which also contain the request
        """
        user = self.request.user
        if not user.is_authenticated:
            return []

        qs = super().get_queryset()

        return qs.filter(user=user)


@api_view(['GET'])
def products_info(request):
    products = Product. Product.objects.prefetch_related('orders').all()
    serializer = ProductsInfoSerializer({
        'products': products,
        'count': products.count(),
        'avg_price': products.aggregate(avg=Avg('price'))['avg']
    })

    return Response(serializer.data)
