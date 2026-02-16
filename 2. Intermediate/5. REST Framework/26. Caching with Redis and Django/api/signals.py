from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from api.models import Product


@receiver([post_delete, post_save], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    """
    Invalidate the product list cache when a product is added or deleted
    """

    cache.delete_pattern("*product_list*")
    