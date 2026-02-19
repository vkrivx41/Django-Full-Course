from django.db import models


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name


    def save(self, **kwargs):
        if self.room_name.count(' ') > 0:
            self.room_name = "_".join(self.room_name.split(" "))

        self.room_name = self.room_name.casefold()

        return super().save(**kwargs)


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content[:15]
    