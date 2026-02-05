from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse


class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class ProductCategories(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        APPLIANCE = "appliance", "Appliance"
        BEAUTY = "beauty", "Beauty"
        CLOTHING = "clothing", "Clothing"
        TRAVEL = "travel", "Travel"

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=30, choices=ProductCategories.choices)
    number_in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    date_posted = models.DateField(default=timezone.now)
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

    def get_absolute_url(self):
        return reverse('products:product', kwargs={
            'slug': self.slug
        })

    