# Python and MongoDB

Every MongoDB topic has an independent `README.md` and runnable `main.py`. Each run uses a unique, randomly named collection and removes only its own sample data.

## Setup

1. Install PyMongo: `python -m pip install -r requirements-databases.txt`.
2. Set `MONGODB_URI` to a local or authorized development database.
3. Do not commit credentials or connect examples to production.

## Topic projects

1. [MongoDB get started](topics/01-mongodb-get-started/README.md) | [Code](topics/01-mongodb-get-started/main.py)
2. [MongoDB create database](topics/02-mongodb-create-database/README.md) | [Code](topics/02-mongodb-create-database/main.py)
3. [MongoDB collection](topics/03-mongodb-collection/README.md) | [Code](topics/03-mongodb-collection/main.py)
4. [MongoDB insert](topics/04-mongodb-insert/README.md) | [Code](topics/04-mongodb-insert/main.py)
5. [MongoDB find](topics/05-mongodb-find/README.md) | [Code](topics/05-mongodb-find/main.py)
6. [MongoDB query](topics/06-mongodb-query/README.md) | [Code](topics/06-mongodb-query/main.py)
7. [MongoDB sort](topics/07-mongodb-sort/README.md) | [Code](topics/07-mongodb-sort/main.py)
8. [MongoDB delete](topics/08-mongodb-delete/README.md) | [Code](topics/08-mongodb-delete/main.py)
9. [MongoDB drop collection](topics/09-mongodb-drop-collection/README.md) | [Code](topics/09-mongodb-drop-collection/main.py)
10. [MongoDB update](topics/10-mongodb-update/README.md) | [Code](topics/10-mongodb-update/main.py)
11. [MongoDB limit](topics/11-mongodb-limit/README.md) | [Code](topics/11-mongodb-limit/main.py)

## Safety

Every topic creates and drops only its uniquely named lesson collection. Never copy cleanup logic to a shared or production collection without reviewing authorization and backup policy.
