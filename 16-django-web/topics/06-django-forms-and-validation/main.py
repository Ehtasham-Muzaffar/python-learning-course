"""Django forms and validation: self-contained Django learning project."""

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
from django import forms

class EnrollmentForm(forms.Form):
    learner = forms.CharField(max_length=40)
    age = forms.IntegerField(min_value=13, max_value=120)

valid = EnrollmentForm({"learner": "Amina", "age": "22"})
invalid = EnrollmentForm({"learner": "Amina", "age": "8"})
print("valid:", valid.is_valid(), valid.cleaned_data if valid.is_valid() else {})
print("invalid errors:", invalid.errors.as_json())
