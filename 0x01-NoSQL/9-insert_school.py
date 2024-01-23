#!/usr/bin/env python3
"""
Define Python function that inserts a new document in a collection based
on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    The function `insert_school` inserts a document into a MongoDB
    collection with the provided keyword arguments and returns the
    inserted document's ID.

    :param mongo_collection: The `mongo_collection` parameter is the
    collection in the MongoDB database where you want to insert the
    school document
    :return: the inserted ID of the document in the MongoDB collection.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
