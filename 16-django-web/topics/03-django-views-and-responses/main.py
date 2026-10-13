"""Django views and responses: self-contained Django learning project."""

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
from django.http import JsonResponse
from django.test import Client
from django.urls import path

def health(request):
    return JsonResponse({"status": "ok"}, status=200)

urlpatterns = [path("health/", health, name="health")]
response = Client().get("/health/")
print("status:", response.status_code, "json:", response.json())
