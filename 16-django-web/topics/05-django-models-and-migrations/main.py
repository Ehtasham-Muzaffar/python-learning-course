"""Django models and migrations: self-contained Django learning project."""

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
from django.db import connection, models

class CourseNote(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        app_label = "lesson_demo"

with connection.schema_editor() as editor:
    editor.create_model(CourseNote)
note = CourseNote.objects.create(title="Model and ORM")
print(CourseNote.objects.get(pk=note.pk).title)
with connection.schema_editor() as editor:
    editor.delete_model(CourseNote)
