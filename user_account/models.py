from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser):
    pass
