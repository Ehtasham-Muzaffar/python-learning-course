# Python and MySQL

Each SQL topic is a separate project with its own README and complete Python entry point. These scripts operate on session-scoped temporary tables, except for the explicitly selected connection schema.

## Setup

1. Install the optional driver: `python -m pip install -r requirements-databases.txt`.
2. Set `MYSQL_HOST`, `MYSQL_PORT` (optional), `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE` for a development database you control.
3. Give the account access only to that schema. Never commit its password.

## Topic projects

1. [MySQL get started](topics/01-mysql-get-started/README.md) | [Code](topics/01-mysql-get-started/main.py)
2. [MySQL create database](topics/02-mysql-create-database/README.md) | [Code](topics/02-mysql-create-database/main.py)
3. [MySQL create table](topics/03-mysql-create-table/README.md) | [Code](topics/03-mysql-create-table/main.py)
4. [MySQL insert](topics/04-mysql-insert/README.md) | [Code](topics/04-mysql-insert/main.py)
5. [MySQL select](topics/05-mysql-select/README.md) | [Code](topics/05-mysql-select/main.py)
6. [MySQL where](topics/06-mysql-where/README.md) | [Code](topics/06-mysql-where/main.py)
7. [MySQL order by](topics/07-mysql-order-by/README.md) | [Code](topics/07-mysql-order-by/main.py)
8. [MySQL delete](topics/08-mysql-delete/README.md) | [Code](topics/08-mysql-delete/main.py)
9. [MySQL drop table](topics/09-mysql-drop-table/README.md) | [Code](topics/09-mysql-drop-table/main.py)
10. [MySQL update](topics/10-mysql-update/README.md) | [Code](topics/10-mysql-update/main.py)
11. [MySQL limit](topics/11-mysql-limit/README.md) | [Code](topics/11-mysql-limit/main.py)
12. [MySQL join](topics/12-mysql-join/README.md) | [Code](topics/12-mysql-join/main.py)

## Safety note

Database creation and persistent `DROP TABLE`/`DROP DATABASE` commands are not automatically run. Do not point a tutorial script at a production database.
