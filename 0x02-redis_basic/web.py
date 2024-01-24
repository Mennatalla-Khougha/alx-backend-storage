#!/usr/bin/env python3
""" implement a get_page function"""
import requests
import redis
from functools import wraps
from typing import Callable


def url_count(method: Callable) -> Callable:
    """
    Decorator that takes a single method Callable argument and returns
    a Callable
    """
    red = redis.Redis()

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function to  increments the count for that key every time
        the method is called
        """
        key = "cached" + url
        value = red.get(key)
        if value:
            return value.decode("utf-8")
        count = "count" + url
        html = method(url)
        red.incr(count)
        red.set(key, html, ex=10)
        red.expire(key, 10)
        return html
    return wrapper


@url_count
def get_page(url: str) -> str:
    """
    It uses the requests module to obtain the HTML content of
    a particular URL and returns i
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
