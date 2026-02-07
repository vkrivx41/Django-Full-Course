from django.db import models
from django.utils import timezone, text
from django.urls import reverse
from django.db.models import Q, F


class Seller(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'male', "Male"
        FEMALE = 'female', "female"

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    phone = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(default="", choices=GenderChoices.choices)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="seller_phone_starts_with_+250",
                condition=Q(phone__startswith="+250"),
            )
        ]

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = text.slugify(self.name)
        
        return super().save(**kwargs)
    
    def get_absolute_url(self):
        return reverse('products:seller', kwargs={
            'slug': self.slug
        })


class Product(models.Model):
    class ProductCategories(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        APPLIANCE = "appliance", "Appliance"
        BEAUTY = "beauty", "Beauty"
        CLOTHING = "clothing", "Clothing"
        TRAVEL = "travel", "Travel"

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    category = models.CharField(max_length=30, choices=ProductCategories.choices)
    number_in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date_posted = models.DateField(default=timezone.now, editable=False)
    seller = models.ForeignKey(to=Seller, on_delete=models.DO_NOTHING, related_name='products')

    class Meta:
        ordering = ['-date_posted', 'name']
        
        constraints = [
            models.UniqueConstraint(
                name='name_seller_unqiue',
                fields=['name', 'seller'],
                violation_error_message='Name and Seller need to be unique at once'
            )
        ]


    def __str__(self):
        return f"{self.name} - {self.number_in_stock}"

    def save(self, **kwargs):
        self.slug = text.slugify(self.name + "-" + str(self.seller.id))
        
        return super().save(**kwargs)
    
    def get_absolute_url(self):
        return reverse('products:product', kwargs={
            'slug': self.slug
        })


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=13, unique=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="buyer_phone_starts_with_+250",
                condition=Q(phone__startswith="+250"),
            )
        ]

    def __str__(self):
        return self.name
    

class Order(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    buyer = models.ForeignKey(to=Buyer, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveSmallIntegerField()
    cost_price = models.PositiveIntegerField(editable=False)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
    def save(self, *args, **kwargs):
        if not self.cost_price:
            self.cost_price = self.product.price * self.quantity

        return super().save(*args, **kwargs)
    