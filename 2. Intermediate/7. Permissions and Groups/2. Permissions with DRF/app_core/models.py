from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="documents")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('publish_document', "Can publish document"),
            ('archive_document', "Can archive document"),
            ('share_document', "Can share document"),
        ]

    def __str__(self):
        return self.title
    

class Subscription(models.Model):
    class SubscriptionType(models.TextChoices):
        FREE = "Free"
        PRO = "Pro"
        Ultra = "Ultra"

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="subscription")
    type = models.CharField(max_length=20, choices=SubscriptionType.choices, default=SubscriptionType.FREE)
    joined_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.type}"
    
