from django.db.models import Avg

from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers import ProductSerializer, OrderSerializer, ProductsInfoSerializer
from api.models import Product, Order, OrderItem


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.prefetch_related(
        'orders', 'items'
    ).all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # the POST data being passed, contains the csrfmiddlewaretoken, when used a user-interface
        return super().create(request, *args, **kwargs)


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


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.prefetch_related('orders').all()

        serializer = ProductsInfoSerializer({
            'products': products,
            'count': products.count(),
            'avg_price': products.aggregate(avg=Avg('price'))['avg']
        })

        return Response(serializer.data)