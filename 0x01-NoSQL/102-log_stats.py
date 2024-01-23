#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    print(f"{db.count_documents({})} logs")
    print("Methods:")

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        print(f"\tmethod {method}: {db.count_documents({'method': method})}")

    status = db.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status} status check")

    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": { "$sum": 1 }
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top = db.aggregate(pipeline)

    print("IPs:")

    for ip in top:
        id = ip['_id']
        count = ip['count']
        print(f"\t{id}: {count}")
