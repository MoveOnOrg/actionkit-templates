from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path

from dsa_actionkit.settings import STATIC_ROOT
from dsa_actionkit.views import (
    event_api_moveon_fake,
    event_search_results,
    index,
    login_context,
    logout,
    user_password_forgot,
)

urlpatterns = [
    re_path(r"^context", login_context),
    re_path(r"^progress", login_context, name="progress"),
    re_path(r"^logout", logout, name="logout"),
    re_path(r"^(?P<name>[-.\w]+)?(/(?P<page>[-.\w]+))?$", index),
    re_path(r"^forgot/$", user_password_forgot, name="user_password_forgot"),
    re_path(r"^cms/event/(?P<page>[-.\w]+)/search_results/", event_search_results, name="event_search_results",),
    re_path(r"^fake/api/events", event_api_moveon_fake, name="event_api_moveon_fake"),
    re_path(r"^fake/stub/reverse", event_api_moveon_fake, name="reverse_donation"),
]
if STATIC_ROOT:
    urlpatterns = staticfiles_urlpatterns()
