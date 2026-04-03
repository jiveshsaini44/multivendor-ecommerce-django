from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['user', 'store_name', 'is_approved']
    list_editable = ['is_approved']