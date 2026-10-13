"""Django security and configuration: self-contained Django learning project."""

from django.conf import settings

if not settings.configured:
    settings.configure(
        SECRET_KEY="local-course-demo-not-for-deployment",
        DEBUG=True,
        ALLOWED_HOSTS=["testserver", "localhost"],
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[],
        MIDDLEWARE=[],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        TEMPLATES=[{"BACKEND": "django.template.backends.django.DjangoTemplates", "APP_DIRS": False, "OPTIONS": {}}],
    )

import django
django.setup()
import os

# Do not provide a fallback production secret or commit a real secret.
secret = os.environ.get("DJANGO_SECRET_KEY")
if not secret:
    print("Set DJANGO_SECRET_KEY through your deployment secret manager.")
else:
    print("A deployment secret is configured; never print its value.")
production_debug = os.environ.get("DJANGO_DEBUG", "false").casefold() == "true"
if production_debug:
    raise RuntimeError("DEBUG must be false in production")
print("This lesson refuses to print secrets or enable production debug mode.")
