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
    