#!/usr/bin/env python
import os
import sys

#STATIC_FALLBACK="/static/js/fallback_local" PYTHONPATH=./djanger django-admin runserver --settings=settings


def serve_templates():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dsa_actionkit.settings")
    sys.path.append(os.getcwd()) # run `aktemplate test` from the same dir where tests live
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    serve_templates()
