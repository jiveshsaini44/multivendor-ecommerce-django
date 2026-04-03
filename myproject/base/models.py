from django.db import models
from django.conf import settings
# Create your models here.

class CartModels(models.Model):
    pname=models.CharField(max_length=100)
    pcategory=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.IntegerField(default=1)
    totalprice=models.IntegerField()
    host=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname    