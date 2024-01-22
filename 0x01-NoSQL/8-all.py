#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    The function "list_all" retrieves all documents from a MongoDB
    collection and returns them as a list.

    :param mongo_collection: The `mongo_collection` parameter is expected
    to be a MongoDB collection object.
    It represents a collection of documents in a MongoDB database
    :return: a list of all documents in the given MongoDB collection.
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
