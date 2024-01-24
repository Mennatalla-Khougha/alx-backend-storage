#!/usr/bin/env python3
"""Create a Cache class"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that takes a single method Callable argument and returns
    a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function to  increments the count for that key every time
        the method is called
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that will add its input parameters to one list in
        redis, and store its output into another list.
        """
        input = str(args)
        self._redis.rpush(key + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ":outputs", output)
        return output

    return wrapper


class Cache:
    """The `Cache` class is a Python class that provides a way to store data
    in a Redis cache and retrieve a unique key for the stored data."""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def get(self, key: str, fn: Callable = None) -> Any:
        """_summary_

        Args:
            key (str): the randomly generated key
            fn (Callable, optional):  will be used to convert the data back
            to the desired format. Defaults to None.

        Returns:
            Any: the desired format
        """
        result = self._redis.get(key)

        if result is None:
            return None

        if fn is not None:
            return fn(result)

        return result

    def get_str(self, key: str) -> str:
        """get_str that will automatically parametrize Cache.get with str

        Args:
            key (str): the randomly generated key

        Returns:
            str: the type of the cache
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """get_int that will automatically parametrize Cache.get with int

        Args:
            key (str): the randomly generated key

        Returns:
            int: the type of the cache
        """
        return self.get(key, fn=int)
