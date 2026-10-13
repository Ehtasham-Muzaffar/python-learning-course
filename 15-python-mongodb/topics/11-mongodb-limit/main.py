"""MongoDB limit: isolated MongoDB mini-project using a unique lesson collection."""

import os
from uuid import uuid4

from pymongo import MongoClient


def main() -> None:
    uri = os.environ.get("MONGODB_URI")
    if not uri:
        raise RuntimeError("Set MONGODB_URI to a local development database.")
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    collection = None
    try:
        client.admin.command("ping")
        database = client["python_course_demo"]
        marker = str(uuid4())
        collection_name = "lesson_mongodb_limit_" + marker[:12]
        collection = database.create_collection(collection_name)
        collection.insert_many([{"marker": marker, "rank": value} for value in [4, 1, 3, 2]])
        rows = list(collection.find({"marker": marker}, {"_id": 0, "rank": 1}).sort("rank", 1).limit(2))
        print("first two sorted records:", rows)
    finally:
        if collection is not None and collection.name in database.list_collection_names():
            collection.drop()
        client.close()


if __name__ == "__main__":
    main()
