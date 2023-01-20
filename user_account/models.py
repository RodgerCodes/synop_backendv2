from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext_lazy as d

# Create your models here.
class Station(models.Model):
    station_name = models.CharField(max_length=100)
    station_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.station_name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=250)
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name="station")
    is_staff = models.BooleanField(
        d('staff status'),
        default=False,
        help_text=d(
            'Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __st__(self):
        return self.email

    
