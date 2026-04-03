from django.db import models
from vendors.models import Vendor

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='products')
    
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=50,default='electronincs')
    
    trending = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name