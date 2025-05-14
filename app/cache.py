# cache.py
import shelve
import os
import time

CACHE_FOLDER = "cache"
CACHE_FILE = os.path.join(CACHE_FOLDER, "github_cache.db")
CACHE_TTL = 3600  # 1 hora por defecto

# Ensure the cache folder exists
os.makedirs(CACHE_FOLDER, exist_ok=True)

def cache_get(key):
    """
    Retrieve a value from cache if not expired.
    """
    with shelve.open(CACHE_FILE) as db:
        record = db.get(key)
        if record:
            value, timestamp = record
            if time.time() - timestamp < CACHE_TTL:
                return value
    return None

def cache_set(key, value):
    """
    Store a value in cache with timestamp.
    """
    with shelve.open(CACHE_FILE) as db:
        db[key] = (value, time.time())

def _force_expired_cache(key, value):
    """
    Used in tests: save a cache value with a forced expiration timestamp.
    """
    with shelve.open(CACHE_FILE) as db:
        db[key] = (value, time.time() - CACHE_TTL - 10)
