import json
import os
import time

try:
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

from django.urls import re_path
from django.conf.urls.static import static
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.static import serve

from .moveon_fakeapi import mo_event_data

"""
try running with
aktemplates runserver 0.0.0.0:1234
"""

DEBUG = True
SECRET_KEY = 'who cares!'
INSTALLED_APPS = ['dsa_actionkit', ]
try:
    INSTALLED_APPS.append('django_extensions')
except:
    pass

#one directory down
APP_PATH = os.path.dirname(__file__)
PROJECT_ROOT_PATH = os.path.abspath(os.getcwd())

#############
# STATIC DIRECTORY
#############

#note this only works if DEBUG=True
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(PROJECT_ROOT_PATH, './static'))
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATIC_FALLBACK = os.environ.get('STATIC_FALLBACK', False)
STATIC_LOCAL = os.environ.get('STATIC_URL', None) # an explicit local or not

#############
# TEMPLATES
#############
DEFAULT_TEMPLATES = os.path.join(APP_PATH, 'templates')
DIR_TEMPLATES = []
if os.environ.get('TEMPLATE_DIR'):
    DIR_TEMPLATES.append(os.environ.get('TEMPLATE_DIR'))
else:
    for d in ('template_set/', '_layouts/', '_includes/'):
        dd = os.path.join(PROJECT_ROOT_PATH, d)
        if os.path.exists(dd):
            DIR_TEMPLATES.append(dd)

DIR_TEMPLATES.append(DEFAULT_TEMPLATES)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': DIR_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': ['dsa_actionkit.templatetags.actionkit_tags'],
        },
    },
]

MIDDLEWARE_CLASSES = []


def _get_context_data(request, name=None, page=None, use_referer=False):
    from dsa_actionkit.contexts.page_contexts import contexts
    port = '4000'
    hostport = request.get_host().split(':')
    if len(hostport) > 1:
        port = hostport[1]

    if use_referer:
        paths = None
        if request.META.get('HTTP_REFERER'):
            paths = urlparse(request.META['HTTP_REFERER']).path.split('/')
        elif request.GET.get('path'):
            # e.g. &path=/events/event_search.html
            paths = request.GET['path'].split('/')
        if paths and len(paths) > 1:
            name = paths[1]
            if len(paths) > 2:
                page = paths[2]

    custom_contexts_file = os.path.join(PROJECT_ROOT_PATH,
                                        os.environ.get('CUSTOM_CONTEXTS', 'contexts.json'))
    if os.path.exists(custom_contexts_file):
        try:
            contexts.update({'Custom': json.loads(open(custom_contexts_file).read())})
        except ValueError as e:
            raise Exception("JSON Parsing Error for context file %s %s" % (
                custom_contexts_file, e.message))
    #first use ?template= if there, otherwise name's template, otherwise homepage
    cxt = dict(
        devenv={
            'enabled': True,
            'port': port,
            'STATIC_URL': STATIC_URL,
            'STATIC_LOCAL': STATIC_LOCAL,
            'MO_EVENTS_API': '/fake/api/events'
        }
    )
    context_data = contexts.get(name, {})
    if page:
        context_data = contexts.get(name, {}).get(page, {})
    cxt.update(context_data)
    if not context_data:
        sections = []
        for section, pages in sorted(contexts.items()):
            sections.append([section, sorted(pages.items())])
        cxt.update({
            'page': {'title':'Homepage'},
            'pagelinks': sections})
    if request.GET.get('user_id'):
        #for debugging tests based on user.id % 2, e.g.
        context_data.setdefault('user', {}).update({'id': int(request.GET.get('user_id'))})
    args = cxt.get('args', {}).copy()
    args.update(request.GET.dict())
    cxt['args'] = args
    if 'akid' not in cxt:
        cxt['akid'] = cxt['args'].get('akid')
    cxt['request'] = request
    cxt['js_context'] = '""' # FUTURE: what should go in here?
    return cxt

#############
# HOME PAGE TEST
#############

def index(request, name=None, page=None):
    cxt = _get_context_data(request, name, page)
    template = request.GET.get('template',
                               cxt.get('filename', "homepagetest.html"))

    return render(request, template, cxt)

def login_context(request):
    cxt = _get_context_data(request, use_referer=True)
    from dsa_actionkit.contexts.event_context_json import event_json
    event_json_copy = event_json.copy()
    coming_from = request.GET.get('url','')
    if 'event' in coming_from \
       or 'logged_in' in coming_from \
       or 'survey_logged_in' in coming_from:
        if not request.GET.get('login') and 'survey_logged_in' not in coming_from:
            del event_json_copy['name']
        return HttpResponse(
            'actionkit.forms.onContextLoaded(%s)' % json.dumps(event_json_copy))
    elif cxt.get('context'):
        return HttpResponse('actionkit.forms.onContextLoaded(%s)' % json.dumps(cxt['context']))
    else:
        return HttpResponse(
            #text key has all the generic error messages
            'actionkit.forms.onContextLoaded({"text": %s})' % json.dumps(event_json['text']))

def user_password_forgot(request):
    return HttpResponse('unimplemented')

def logout(request):
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect('/logout.html')

def event_search_results(request, page):
    cxt = _get_context_data(request, 'events', 'WILL_USE_REFERER_HEADER', use_referer=True)
    # special query results context:
    all = cxt['args'].get('all') == '1'
    cxt.update({'all': all})
    if cxt.get('SLOW_SEARCH'):
        # This allows us to test for race conditions
        time.sleep(2)
    search_results = render_to_string('event_search_results.html', cxt)
    return HttpResponse('actionkit.forms.onEventSearchResults({})'
                        .format(json.dumps(search_results)))

def event_api_moveon_fake(request):
    """Fake representation of MoveOn events api"""
    cxt = _get_context_data(request, 'events', 'WILL_USE_REFERER_HEADER', use_referer=True)
    events = cxt.get('events', [])
    if cxt.get('SLOW_API'):
        # This allows us to test for race conditions
        time.sleep(2)
    if cxt.get('500_API'):
        raise Exception('Cause failure to allow graceful degradation')
    search_results = [mo_event_data(evt) for evt in events]
    return HttpResponse(json.dumps({'events': search_results}), content_type='application/json')

def proxy_serve(request, path, document_root=None, show_indexes=False):
    try_proxy = True
    try:
        import requests
    except ImportError:
        try_proxy = False
    try:
        return serve(request, path, document_root, show_indexes)
    except Http404:
        if try_proxy:
            prefix = request.path.split('/')[1]
            content = requests.get('https://roboticdogs.actionkit.com/{}/{}'.format(prefix, path), verify=False)
            if content.status_code == 200:
                return HttpResponse(content.content, content_type=content.headers['Content-Type'])
    raise Http404




if os.path.exists(os.path.join(PROJECT_ROOT_PATH, 'local_settings.py')):
    from local_settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite",
    }
}