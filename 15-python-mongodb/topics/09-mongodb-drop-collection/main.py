"""MongoDB drop collection: isolated MongoDB mini-project using a unique lesson collection."""

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
        collection_name = "lesson_mongodb_drop_collection_" + marker[:12]
        collection = database.create_collection(collection_name)
        collection.insert_one({"marker": marker, "topic": "drop demonstration"})
        collection_name = collection.name
        collection.drop()
        print("dropped only unique lesson collection:", collection_name)
    finally:
        if collection is not None and collection.name in database.list_collection_names():
            collection.drop()
        client.close()


if __name__ == "__main__":
    main()
