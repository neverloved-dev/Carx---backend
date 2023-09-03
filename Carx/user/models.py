from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length = 125,null=False)
    last_name = models.CharField(max_length=125,null=False)
    email = models.CharField(max_length=125,null = True)
    phone_number = models.CharField(max_length=12, null=False)