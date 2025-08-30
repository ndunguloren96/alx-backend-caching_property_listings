from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

@receiver(post_save, sender=Property)
def invalidate_property_cache_on_save(sender, instance, **kwargs):
    """
    Signal handler to invalidate the 'all_properties' cache key
    whenever a Property object is saved (created or updated).
    """
    cache.delete('all_properties')
    print("Cache 'all_properties' invalidated due to a save operation.")

@receiver(post_delete, sender=Property)
def invalidate_property_cache_on_delete(sender, instance, **kwargs):
    """
    Signal handler to invalidate the 'all_properties' cache key
    whenever a Property object is deleted.
    """
    cache.delete('all_properties')
    print("Cache 'all_properties' invalidated due to a delete operation.")
