from django.core.cache import cache
from .models import Property
import logging
from django.core.cache import cache

# Set up logging
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Connects to Redis to retrieve keyspace hits and misses,
    calculates the hit ratio, and logs the metrics.
    """
    try:
        # Get the underlying Redis client from the cache backend
        redis_client = cache.client.get_client(None)
        
        # Get Redis INFO to find keyspace stats
        info = redis_client.info('stats')
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)
        
        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total_requests) * 100 if total_requests > 0 else 0
        
        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'hit_ratio_percent': round(hit_ratio, 2),
        }
        
        logger.info("Redis Cache Metrics: %s", metrics)
        return metrics
    except Exception as e:
        logger.error(f"Failed to get Redis metrics: {e}")
        return {}

def get_all_properties():
    """
    Fetches all properties from the cache, or from the database if not cached.
    The queryset is cached for 1 hour (3600 seconds).
    """
    all_properties = cache.get('all_properties')
    if not all_properties:
        all_properties = list(Property.objects.all())
        cache.set('all_properties', all_properties, 3600)
    return all_properties
