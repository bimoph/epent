from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()

class User(AbstractUser):
    # is_admin= models.BooleanField('Is admin', default=False)
    is_EO = models.BooleanField('Is EO', default=False)
    is_company = models.BooleanField('Is company', default=False)

class User_EO(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_event = models.CharField(max_length=50)
    email = models.EmailField()


class User_company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_company = models.CharField(max_length=50)
    email = models.EmailField()

