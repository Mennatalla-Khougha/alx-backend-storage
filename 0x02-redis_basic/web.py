#!/usr/bin/env python3
"""Implement a get_page function."""
import redis
import requests
from functools import wraps

red = redis.Redis()


def url_count(method):
    """decorator for get_page function"""
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        key = "cached:" + url
        value = red.get(key)
        if value:
            return value.decode("utf-8")

        count = "count:" + url
        html = method(url)

        red.incr(count)
        red.set(key, html, ex=10)
        red.expire(key, 10)
        return html
    return wrapper


@url_count
def get_page(url: str) -> str:
    """obtain the HTML content"""
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
