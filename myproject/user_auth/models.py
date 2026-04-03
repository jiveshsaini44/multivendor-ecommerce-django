from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES_CHOICES=(
        ('buyer','Buyer'),
        ('vendor','Vendor'),
    )
    role=models.CharField(max_length=10, choices=ROLES_CHOICES)
    
    def __str__(self):
        return self.username
    
    