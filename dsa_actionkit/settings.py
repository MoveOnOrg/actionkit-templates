import contextlib
import os
from pathlib import Path

DEBUG = True
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
INSTALLED_APPS = ["dsa_actionkit" ]
with contextlib.suppress(Exception):
    INSTALLED_APPS.append("django_extensions")

ROOT_URLCONF = "dsa_actionkit.urls"
APP_PATH = Path().parent
PROJECT_ROOT_PATH = Path.resolve(Path.cwd())

STATIC_ROOT = os.environ.get("STATIC_ROOT", PROJECT_ROOT_PATH / "static")
STATIC_URL = os.environ.get("STATIC_URL", "/static/")
STATIC_FALLBACK = os.environ.get("STATIC_FALLBACK", False)
STATIC_LOCAL = os.environ.get("STATIC_URL", None)
DEFAULT_TEMPLATES = APP_PATH / "templates"
DIR_TEMPLATES = []
if os.environ.get("TEMPLATE_DIR"):
    DIR_TEMPLATES.append(os.environ.get("TEMPLATE_DIR"))
else:
    for d in ("template_set/", "_layouts/", "_includes/"):
        dd = PROJECT_ROOT_PATH / d
        if Path.exists(dd):
            DIR_TEMPLATES.append(dd)

DIR_TEMPLATES.append(DEFAULT_TEMPLATES)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": DIR_TEMPLATES,
        "APP_DIRS": True,
        "OPTIONS": {
            "builtins": ["dsa_actionkit.templatetags.actionkit_tags"],
        },
    },
]

MIDDLEWARE_CLASSES = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite",
    },
}
