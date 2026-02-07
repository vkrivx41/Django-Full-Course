from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.utils import text
from django.urls import reverse
from django.contrib.sites.models import Site
from django.conf import settings
from django.core import mail

from products.models import Product, Order, ProductBackUp

from services.EmailService import EmailService


@receiver(pre_save, sender=Product)
def product_pre_save_signal(instance, **kwargs):
    if not instance.slug:
        instance.slug = text.slugify(instance.name + "-" + str(instance.seller.id))


@receiver(post_save, sender=Order)
def order_post_save_signal(instance, created, **kwargs):
    if created:
        protocol = settings.SITE_PROTOCOL
        domain = Site.objects.get_current().domain
        relative_url = reverse('products:orders')

        full_url = f"{protocol}://{domain}{relative_url}"

        EmailService().send_email(context={
            'buyer': instance.buyer,
            'order': instance,
            'orders_url': full_url,
        })

def product_pre_delete_signal(instance, **kwargs):
    product_back_up = ProductBackUp(
        name=instance.name,
        category=instance.category,
        price=instance.price,
        date_posted=instance.date_posted,
        seller=instance.seller.pk,
    )

    product_back_up.save()
pre_delete.connect(product_pre_delete_signal, sender=Product)


def product_post_delete_signal(instance, **kwargs):
    mail.send_mail(
        subject="Product Deletion",
        message="Product has been Deleted Successfully",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_HOST_USER],
    )
    
post_delete.connect(product_post_delete_signal, sender=Product)