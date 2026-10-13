# Django views and responses

**Purpose and use:** A view validates a request and returns an HTTP response. Keep domain rules testable and avoid including secrets in responses.

## Project walkthrough

This is a complete runnable Django example. The project uses explicit, in-memory development settings so it can demonstrate **Django views and responses** without requiring a deployed site or real database. Read each statement, change a safe input, and inspect the response or validation result.

## Run

Install the optional Django dependency and run from the repository root:

```bash
python 16-django-web/topics/03-django-views-and-responses/main.py
```

## Practice

Extend the example with a small automated test. Keep secrets in environment/deployment configuration and do not expose Django's development server to the public internet.

**Related track:** [Django topic index](../../README.md) | [Course home](../../../README.md)
