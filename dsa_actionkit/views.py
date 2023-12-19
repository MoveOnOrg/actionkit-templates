import json
import os
import time
from pathlib import Path
from urllib import parse

import requests
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.static import serve

from dsa_actionkit.moveon_fakeapi import mo_event_data


def _get_context_data(request, name=None, page=None, use_referer=False):
    from dsa_actionkit.contexts.page_contexts import contexts
    port = "4000"
    hostport = request.get_host().split(":")
    if len(hostport) > 1:
        port = hostport[1]

    if use_referer:
        paths = None
        if request.META.get("HTTP_REFERER"):
            paths = parse(request.META["HTTP_REFERER"]).path.split("/")
        elif request.GET.get("path"):
            paths = request.GET["path"].split("/")
        if paths and len(paths) > 1:
            name = paths[1]
            if len(paths) > 2:
                page = paths[2]

    custom_contexts_file = settings.PROJECT_ROOT_PATH / os.environ.get(
        "CUSTOM_CONTEXTS",
        "contexts.json",
    )
    if Path.exists(custom_contexts_file):
        try:
            contexts.update({"Custom": json.loads(open(custom_contexts_file).read())})
        except ValueError as e:
            msg = (
                "JSON Parsing Error for context file {} {}".format(
                custom_contexts_file, e.message)
            )
            raise Exception(msg)
    #first use ?template= if there, otherwise name's template, otherwise homepage
    cxt = {
        "devenv": {
            "enabled": True,
            "port": port,
            "STATIC_URL": settings.STATIC_URL,
            "STATIC_LOCAL": settings.STATIC_LOCAL,
            "MO_EVENTS_API": "/fake/api/events",
        },
    }
    context_data = contexts.get(name, {})
    if page:
        context_data = contexts.get(name, {}).get(page, {})
    cxt.update(context_data)
    if not context_data:
        sections = []
        for section, pages in sorted(contexts.items()):
            sections.append([section, sorted(pages.items())])
        cxt.update({
            "page": {"title":"Homepage"},
            "pagelinks": sections})
    if request.GET.get("user_id"):
        #for debugging tests based on user.id % 2, e.g.
        context_data.setdefault("user", {}).update({"id": int(request.GET.get("user_id"))})
    args = cxt.get("args", {}).copy()
    args.update(request.GET.dict())
    cxt["args"] = args
    if "akid" not in cxt:
        cxt["akid"] = cxt["args"].get("akid")
    cxt["request"] = request
    cxt["js_context"] = '""' # FUTURE: what should go in here?
    return cxt


def index(request, name=None, page=None):
    cxt = _get_context_data(request, name, page)
    template = request.GET.get("template",
                               cxt.get("filename", "homepagetest.html"))

    return render(request, template, cxt)

def login_context(request):
    cxt = _get_context_data(request, use_referer=True)
    from dsa_actionkit.contexts.event_context_json import event_json
    event_json_copy = event_json.copy()
    coming_from = request.GET.get("url","")
    if "event" in coming_from \
       or "logged_in" in coming_from \
       or "survey_logged_in" in coming_from:
        if not request.GET.get("login") and "survey_logged_in" not in coming_from:
            del event_json_copy["name"]
        return HttpResponse(
            "actionkit.forms.onContextLoaded(%s)" % json.dumps(event_json_copy))
    elif cxt.get("context"):
        return HttpResponse("actionkit.forms.onContextLoaded(%s)" % json.dumps(cxt["context"]))
    else:
        return HttpResponse(
            #text key has all the generic error messages
            'actionkit.forms.onContextLoaded({"text": %s})' % json.dumps(event_json["text"]))

def user_password_forgot(request):
    return HttpResponse("unimplemented")

def logout(request):
    if request.GET.get("next"):
        return redirect(request.GET.get("next"))
    return redirect("/logout.html")

def event_search_results(request, page):
    cxt = _get_context_data(request, "events", "WILL_USE_REFERER_HEADER", use_referer=True)
    # special query results context:
    all = cxt["args"].get("all") == "1"
    cxt.update({"all": all})
    if cxt.get("SLOW_SEARCH"):
        # This allows us to test for race conditions
        time.sleep(2)
    search_results = render(request, "event_search_results.html", cxt)
    return HttpResponse("actionkit.forms.onEventSearchResults({})"
                        .format(json.dumps(search_results)))

def event_api_moveon_fake(request):
    """Fake representation of MoveOn events api"""
    cxt = _get_context_data(request, "events", "WILL_USE_REFERER_HEADER", use_referer=True)
    events = cxt.get("events", [])
    if cxt.get("SLOW_API"):
        # This allows us to test for race conditions
        time.sleep(2)
    if cxt.get("500_API"):
        raise Exception("Cause failure to allow graceful degradation")
    search_results = [mo_event_data(evt) for evt in events]
    return HttpResponse(json.dumps({"events": search_results}), content_type="application/json")

def proxy_serve(request, path, document_root=None, show_indexes=False):

    try:
        return serve(request, path, document_root, show_indexes)
    except Http404:
        prefix = request.path.split("/")[1]
        content = requests.get(
            f"https://roboticdogs.actionkit.com/{prefix}/{path}",
            verify=False,
            timeout=10,
        )
        if content.status_code == 200:
            return HttpResponse(content.content, content_type=content.headers["Content-Type"])
    raise Http404
