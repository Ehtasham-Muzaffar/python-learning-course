# MySQL create database

**Purpose and use:** Create a named schema during deliberate environment provisioning. This lesson verifies the selected schema and does not create or drop databases automatically.

## Project walkthrough

`main.py` connects with environment-based settings, creates a temporary example table limited to the current connection, and runs the `CREATE DATABASE` operation with bound SQL parameters. Temporary tables vanish when the session closes; the script does not remove your database or persistent tables.

## Configure and run

Install `mysql-connector-python`, set the five `MYSQL_*` variables to a development schema that already exists, then run from the repository root:

```bash
python 14-python-mysql/topics/02-mysql-create-database/main.py
```

## Practice

Change the example input, predict the query result, then inspect `cursor.rowcount` or the returned rows. For any persistent-table operation, use migrations, backups, and explicit authorization.

**Related track:** [MySQL topic index](../../README.md) | [Course home](../../../README.md)
