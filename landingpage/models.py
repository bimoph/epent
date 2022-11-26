from django.db import models
from django.contrib.auth.models import (
BaseUserManager, AbstractBaseUser
)
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    title  = models.CharField(max_length=50)
    deskripsi = models.TextField()