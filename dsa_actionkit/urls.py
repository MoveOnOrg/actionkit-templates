from django.urls import re_path

from dsa_actionkit.views import login_context

urlpatterns = [
    re_path(r"^context", login_context),
    re_path(r"^progress", login_context, name="progress"),
    re_path(r"^logout", logout, name="logout"),
    re_path(r"^(?P<name>[-.\w]+)?(/(?P<page>[-.\w]+))?$", index),
    re_path(r"^forgot/$", user_password_forgot, name="user_password_forgot"),
    re_path(r"^cms/event/(?P<page>[-.\w]+)/search_results/", event_search_results, name="event_search_results"),
    re_path(r"^fake/api/events", event_api_moveon_fake, name="event_api_moveon_fake"),
    # ActionKit urls or {% url %} template tag:
    re_path(r"^fake/stub/reverse", event_api_moveon_fake, name="reverse_donation"),
]
if STATIC_ROOT:
    urlpatterns = (urlpatterns
                   + static(STATIC_URL, document_root=STATIC_ROOT)
                   + static("/resources/",
                            view=proxy_serve,
                            document_root=os.path.join(STATIC_ROOT, "./resources"))
                   + static("/media/",
                            view=proxy_serve,
                            document_root=os.path.join(STATIC_ROOT, "./media"))
    )
