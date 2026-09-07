from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    username = models.EmailField(max_length=100, unique=True)
    email = models.CharField(unique=True)
    phone = models.CharField(max_length=100,  null=True, blank=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username
    

