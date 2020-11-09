from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CostControlUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=False, default='', name='First name')
    registration_date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )
