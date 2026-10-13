# Django templates

**Purpose and use:** Templates render presentation from context. Automatic escaping helps protect HTML; never mark untrusted input safe without sanitization.

## Project walkthrough

This is a complete runnable Django example. The project uses explicit, in-memory development settings so it can demonstrate **Django templates** without requiring a deployed site or real database. Read each statement, change a safe input, and inspect the response or validation result.

## Run

Install the optional Django dependency and run from the repository root:

```bash
python 16-django-web/topics/04-django-templates/main.py
```

## Practice

Extend the example with a small automated test. Keep secrets in environment/deployment configuration and do not expose Django's development server to the public internet.

**Related track:** [Django topic index](../../README.md) | [Course home](../../../README.md)
