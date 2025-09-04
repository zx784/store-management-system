from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    ROLES =[
    ('Admin', 'admin'),
    ('User', 'user'),


    ]

    role = models.CharField(max_length=20, choices= ROLES, default='user')
# Create your models here.
    def __str__(self):
        return self.username