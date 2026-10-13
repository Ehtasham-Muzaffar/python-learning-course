# MongoDB query

**Purpose and use:** MongoDB query operators express comparisons. Validate external input before using it to construct a query.

## Project walkthrough

`main.py` connects with `MONGODB_URI`, creates a collection with a fresh random name, demonstrates this topic, and cleans up only that unique collection. This isolates the exercise from existing collections.

## Run

Install PyMongo and configure a development URI, then run from the repository root:

```bash
python 15-python-mongodb/topics/06-mongodb-query/main.py
```

## Practice

Change the document fields or filter, predict the returned records, then verify the result. Review the cleanup filter before adapting this project to persistent collections.

**Related track:** [MongoDB topic index](../../README.md) | [Course home](../../../README.md)
