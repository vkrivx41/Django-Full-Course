from django.db.models import Avg

from rest_framework import generics, filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilter, OrderFilter
from api.serializers import ProductSerializer, OrderSerializer, ProductsInfoSerializer, OrderCreateSerializer
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

    pagination_class = PageNumberPagination
    pagination_class.page_size = 3
    pagination_class.page_query_param = 'pagenum'
    pagination_class.page_size_query_param = 'length'  # param for setting the page size (no. of results)
    pagination_class.max_page_size = 10  # the max size of the page (size query param can't override this)

    # set for the LimitOffsetPagination
    # pagination_class.default_limit = 3  # the size of the page
    # pagination_class.limit_query_param = 'size'


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


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related(
        'items', 'items__product'
    ).all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = OrderFilter
    search_fields = ['status', 'product__name', 'user__username']

    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        # can also use the self.request.method == "POST"
        if self.action in ["create", "update"]:
            return OrderCreateSerializer
        
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        current_queryset = super().get_queryset()

        if not user.is_staff:
            current_queryset = current_queryset.filter(user=user)
        
        return current_queryset

    @action(
        detail=False,
        methods=['GET'],
        url_path='user-orders',
        permission_classes=[IsAuthenticated]
    )
    def user_orders(self, request):
        user = request.user
        orders = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(orders, many=True)

        return Response(serializer.data)


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.prefetch_related('orders').all()

        serializer = ProductsInfoSerializer({
            'products': products,
            'count': products.count(),
            'avg_price': products.aggregate(avg=Avg('price'))['avg']
        })

        return Response(serializer.data)