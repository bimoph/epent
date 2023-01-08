from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()

class User(AbstractUser):
    # is_admin= models.BooleanField('Is admin', default=False)
    is_EO = models.BooleanField('Is EO', default=False)
    is_company = models.BooleanField('Is company', default=False)

class Event(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_event = models.CharField(max_length=50)
    logo_image = models.ImageField(blank=True, null=True, upload_to="images/")
    email = models.EmailField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    link_linkedin = models.CharField(max_length=50, blank=True, null=True)
    link_instagram = models.CharField(max_length=50, blank=True, null=True)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_company = models.CharField(max_length=50)
    logo_image = models.ImageField(blank=True, null=True, upload_to="images/")
    bidang_usaha = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    link_linkedin = models.CharField(max_length=50, blank=True, null=True)
    link_instagram = models.CharField(max_length=50, blank=True, null=True)

