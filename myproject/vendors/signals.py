from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Vendor

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_vendor_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'vendor':
        Vendor.objects.create(
            user=instance,
            store_name=f"{instance.username}'s Store"
        )