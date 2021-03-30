from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    picture = models.URLField()


class Message(models.Model):
    messager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg")
    content = models.TextField()


class ChatRoom(models.Model):
    members = models.ManyToManyField(User, symmetrical=False)
    messages = models.ManyToManyField(Message, symmetrical=False)