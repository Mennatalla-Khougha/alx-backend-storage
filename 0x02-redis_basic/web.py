#!/usr/bin/env python3
"""Implement a get_page function."""
import redis
import requests
from functools import wraps

r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ track how many times a particular URL was accessed in the key
        "count:{url}"
        and cache the result with an expiration time of 10 seconds """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text

# def url_count(method):
#     """Decorator for get_page function"""
#     @wraps(method)
#     def wrapper(url):
#         """Wrapper function"""
#         red.incr(f"count:{url}")
#         value = red.get(f"cached:{url}")
#         if value:
#             return value.decode("utf-8")

#         html = method(url)
#         red.setex(f"cached:{url}", 10, html)
#         # red.set(f"cached:{url}", html)
#         # red.expire(f"cached:{url}", 10)
#         # red.setex(f"cached:{url}", 10, html)
#         return html
#     return wrapper


# @url_count
# def get_page(url: str) -> str:
#     """obtain the HTML content"""
#     results = requests.get(url)
#     return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
