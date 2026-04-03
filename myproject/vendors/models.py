

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    
    store_name = models.CharField(max_length=255)
    store_description = models.TextField(blank=True)
    
    is_approved = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name