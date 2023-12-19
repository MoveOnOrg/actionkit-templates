import os

try:
    from urlparse import urlparse
except ImportError:
    # python3
    pass



DEBUG = True
SECRET_KEY = "who cares!"
INSTALLED_APPS = ["dsa_actionkit" ]
try:
    INSTALLED_APPS.append("django_extensions")
except:
    pass

ROOT_URLCONF = "dsa_actionkit.urls"
#one directory down
APP_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.abspath(os.getcwd())

#############
# STATIC DIRECTORY
#############

#note this only works if DEBUG=True
STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(PROJECT_ROOT_PATH, "./static"))
STATIC_URL = os.environ.get("STATIC_URL", "/static/")
STATIC_FALLBACK = os.environ.get("STATIC_FALLBACK", False)
STATIC_LOCAL = os.environ.get("STATIC_URL", None) # an explicit local or not

#############
# TEMPLATES
#############
DEFAULT_TEMPLATES = os.path.join(APP_PATH, "templates")
DIR_TEMPLATES = []
if os.environ.get("TEMPLATE_DIR"):
    DIR_TEMPLATES.append(os.environ.get("TEMPLATE_DIR"))
else:
    for d in ("template_set/", "_layouts/", "_includes/"):
        dd = os.path.join(PROJECT_ROOT_PATH, d)
        if os.path.exists(dd):
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


#############
# HOME PAGE TEST
#############


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite",
    },
}
