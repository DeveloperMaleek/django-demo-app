from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class OkUser(BaseUserManager):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)