from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['vendor']  # Exclude the vendor field since it will be set in the view