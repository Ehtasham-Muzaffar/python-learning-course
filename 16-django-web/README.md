# Django Python Web Development

Each topic has its own runnable Django mini-project. The examples configure in-memory settings for learning and do not start a public server.

## Setup

1. Install Django: `python -m pip install -r requirements-web.txt`.
2. Run a topic from the repository root using the command in its README.
3. For a full app scaffold, see the Django startproject and startapp commands in the category overview.

## Topic projects

1. [Django get started](topics/01-django-get-started/README.md) | [Code](topics/01-django-get-started/main.py)
2. [Django URL routing](topics/02-django-url-routing/README.md) | [Code](topics/02-django-url-routing/main.py)
3. [Django views and responses](topics/03-django-views-and-responses/README.md) | [Code](topics/03-django-views-and-responses/main.py)
4. [Django templates](topics/04-django-templates/README.md) | [Code](topics/04-django-templates/main.py)
5. [Django models and migrations](topics/05-django-models-and-migrations/README.md) | [Code](topics/05-django-models-and-migrations/main.py)
6. [Django forms and validation](topics/06-django-forms-and-validation/README.md) | [Code](topics/06-django-forms-and-validation/main.py)
7. [Django admin](topics/07-django-admin/README.md) | [Code](topics/07-django-admin/main.py)
8. [Django security and configuration](topics/08-django-security-and-configuration/README.md) | [Code](topics/08-django-security-and-configuration/main.py)

## Start a conventional Django project

For a persistent application project, use a virtual environment and run `django-admin startproject config django-course-demo`, then `python manage.py startapp lessons` from that directory. The mini-projects here stay independent and do not replace the standard Django project structure.
