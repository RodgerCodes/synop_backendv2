from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.
class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.station_name


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __st__(self):
        return self.email

    
