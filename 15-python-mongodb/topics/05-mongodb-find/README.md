# MongoDB find

**Purpose and use:** Find documents with a filter and a projection that returns only needed fields.

## Project walkthrough

`main.py` connects with `MONGODB_URI`, creates a collection with a fresh random name, demonstrates this topic, and cleans up only that unique collection. This isolates the exercise from existing collections.

## Run

Install PyMongo and configure a development URI, then run from the repository root:

```bash
python 15-python-mongodb/topics/05-mongodb-find/main.py
```

## Practice

Change the document fields or filter, predict the returned records, then verify the result. Review the cleanup filter before adapting this project to persistent collections.

**Related track:** [MongoDB topic index](../../README.md) | [Course home](../../../README.md)
