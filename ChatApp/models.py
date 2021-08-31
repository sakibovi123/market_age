from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class ChatRoom(models.Model):
    slug = models.SlugField(null=True)
    welcome_msg = models.CharField(max_length=120, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    # message = models.TextField()
    
    def __str__(self):
        return str(self.sender)
    


class Message(models.Model):
    chatroom = models.OneToOneField(ChatRoom, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="asd")
    messages = models.TextField()
    

