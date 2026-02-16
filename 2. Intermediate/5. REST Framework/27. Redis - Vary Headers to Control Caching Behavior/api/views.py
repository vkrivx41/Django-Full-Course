from django.db.models import Avg
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

import time

from api.filters import ProductFilter
from api.serializers import ProductSerializer, OrderSerializer, ProductsInfoSerializer
from api.models import Product, Order, OrderItem


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.prefetch_related(
        'orders', 'items'
    ).all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    
    search_fields = ['name', 'description', 'stock'] # works on text fields (CharField, TextField) by convention
    ordering_fields = ['name', 'price', 'stock']
    # filterset_fields = ('name', 'price')  # put in a FilterSet class as fields

    pagination_class = None

    @method_decorator(cache_page(60 * 15, key_prefix="product_list"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        time.sleep(2)  # simulate a DB query delay
        return super().get_queryset()
    
    def get_permissions(self):
        """
        Overridding the get_permissions method to set admin authorization for POST requests
        :param self: the View
        """
        self.permission_classes = [AllowAny]

        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()


class ProductCreateAPIView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # the POST data being passed, contains the csrfmiddlewaretoken, when used a user-interface
        return super().create(request, *args, **kwargs)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related('orders')
    serializer_class = ProductSerializer

    # lookup_field = 'id'  # the field name to lookup for products/<int:id>
    # lookup_field = 'name'  # the field name to lookup for products/<str:name>

    lookup_url_kwarg = 'product_id'  # the name of the dynamic url lookup products/<int:product_id>

    def get_permissions(self):
        self.permission_classes = [AllowAny]

        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
            
        return super().get_permissions()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    lookup_url_kwarg = 'pro_id'


class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'product__name']  # search can include foreign keys


class UserOrderListApiView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 15, key_prefix="user_order_list"))
    @method_decorator(vary_on_headers("Authorization"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        print("sleeping for 15 seconds")
        time.sleep(15)  # simulate a DB query delay
        return super().get_queryset()
    
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