#!/usr/bin/env python3
"""function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    The function `top_students` takes a MongoDB collection as input and
    returns a sorted list of students based on their average score.

    :param mongo_collection: The `mongo_collection` parameter is the
    collection in MongoDB that contains the student data. It is the
    collection that you want to query and perform the aggregation on
    :return: the result of the aggregation pipeline on the given MongoDB
    collection. The result will be a cursor object that can be iterated
    over to access the documents in the result set.
    """
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
