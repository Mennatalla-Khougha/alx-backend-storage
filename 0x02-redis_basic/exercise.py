#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """The `Cache` class is a Python class that provides a way to store data
    in a Redis cache and retrieve a unique key for the stored data."""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string. The method should
        generate a random key, store the input data in Redis using the
        random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): An argument

        Returns:
            str: the generated random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
