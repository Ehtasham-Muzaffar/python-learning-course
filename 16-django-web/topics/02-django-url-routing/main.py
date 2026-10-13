"""Django URL routing: self-contained Django learning project."""

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
from django.http import HttpResponse
from django.test import Client
from django.urls import path, reverse

def lesson_detail(request, lesson_id):
    return HttpResponse(f"Lesson {lesson_id}")

urlpatterns = [path("lessons/<int:lesson_id>/", lesson_detail, name="lesson-detail")]
path = reverse("lesson-detail", kwargs={"lesson_id": 7})
print("reversed URL:", path, "response:", Client().get(path).content.decode())
