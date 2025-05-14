import pytest
import time
from app.cache import cache_get, cache_set, _force_expired_cache


def test_cache_set_and_get():
    """
    Test that values are correctly set and retrieved from the cache.
    """
    url = "https://api.github.com/test/cache"
    payload = {"key": "value"}

    # Set value in cache
    cache_set(url, payload)
    result = cache_get(url)

    assert result == payload


def test_cache_expiration():
    url = "https://api.github.com/test/expire"
    payload = {"expired": True}

    _force_expired_cache(url, payload)
    result = cache_get(url)

    assert result is None


def test_cache_is_isolated():
    """
    Ensure different URLs do not interfere in cache.
    """
    url1 = "https://api.github.com/test/1"
    url2 = "https://api.github.com/test/2"
    val1 = {"one": 1}
    val2 = {"two": 2}

    cache_set(url1, val1)
    cache_set(url2, val2)

    assert cache_get(url1) == val1
    assert cache_get(url2) == val2
