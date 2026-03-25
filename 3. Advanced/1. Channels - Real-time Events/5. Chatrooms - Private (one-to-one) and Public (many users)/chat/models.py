from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(to=User, through="PrivateRoom")

    def __str__(self):
        return self.room_name


    def save(self, **kwargs):
        if self.room_name.count(' ') > 0:
            self.room_name = "_".join(self.room_name.split(" "))

        self.room_name = self.room_name.casefold()

        return super().save(**kwargs)
    
    def display_name(self, user):
        for chatter in self.users:
            if chatter != user:
                return chatter 


class PrivateRoom(models.Model):
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['room']),
            models.Index(fields=['user']),
        ]
        
        constraints = [
            models.UniqueConstraint(
                name='room_user_unique',
                fields=['room', 'user'],
                violation_error_message="Room and User must be unique"
            )
        ]

    def __str__(self):
        return f"{self.room} - {self.user}"


class Message(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="sents")
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content[:15]
    