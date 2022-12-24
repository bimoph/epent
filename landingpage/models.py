from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class user_EO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_event = models.CharField(max_length=50)
    email = models.EmailField()


class user_company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_company = models.CharField(max_length=50)
    email = models.EmailField()

