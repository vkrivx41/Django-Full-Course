from django.db import transaction

from rest_framework import serializers

from api.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock')

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must greater than 0")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()  # include all fields of the product
    # product = serializers.StringRelatedField()  # includes only the value from __str__
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        source='product.price',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity')
    

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(read_only=True)
    # total_price = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = Order
        fields = ('order_id', 'user', 'created_at', 'status', 'items', 'total_price')
    

    # this can be called anything if it will be passed as the method_name
    # def total(self, obj):
    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(item.item_subtotal for item in order_items)
    

class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerilaizer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ('product', 'quantity')

    items = OrderItemCreateSerilaizer(many=True)

    class Meta:
        model = Order
        fields = ('order_id', 'user', 'status', 'items')
        read_only_fields = ('orders_id',)

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        items = validated_data.pop('items')

        with transaction.atomic():
            order = Order.objects.create(**validated_data)

            for item in items:
                OrderItem.objects.create(
                    order=order,
                    **item
                )

        return order
    
    def update(self, instance, validated_data):
        items = validated_data.pop('items')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            if items:
                # clearing existing item (this depends on the business logic)
                instance.items.all().delete()
                    
                for item in items:
                    OrderItem.objects.create(
                        order=instance,
                        **item
                    )
        return instance


class ProductsInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True, read_only=True)
    count = serializers.IntegerField()
    avg_price = serializers.FloatField()
