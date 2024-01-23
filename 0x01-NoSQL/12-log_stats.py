#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    print(f"{logs.count_documents({})} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print(f"\tmethod{method}: {logs.count_documents({'method': method})}")

    status = logs.count_documents({"method": "GET", 'path': '/status'})
    print(f"{status} status check")
