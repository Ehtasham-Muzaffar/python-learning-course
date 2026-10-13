"""Django admin: self-contained Django learning project."""

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
from django.contrib import admin
from django.db import models

class CourseNote(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        app_label = "lesson_demo"

class CourseNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)

# Registration is intentionally shown without starting a server or creating users.
print("Admin list columns:", CourseNoteAdmin.list_display)
print("Site registration uses admin.site.register(CourseNote, CourseNoteAdmin).")
