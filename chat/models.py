from django.db import models
from django.dispatch import receiver
from django.http import request
from django.contrib.auth.models import User
from landingpage.models import User


class Massage(models.Model):
    sender = models.ForeignKey(User, related_name='sender_messages',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    massage = models.CharField(max_length=50)
    isRead = models.BooleanField
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date",)