import json
import os
import re
import sys
import time
try:
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

from django.conf.urls import url
from django.conf.urls.static import static
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.template.base import add_to_builtins
from django.views.static import serve
from .moveon_fakeapi import mo_event_data

"""
try running with
aktemplates runserver 0.0.0.0:1234
"""

DEBUG = True
SECRET_KEY = 'who cares!'
INSTALLED_APPS = ['actionkit_templates', ]
try:
    import template_debug #django-template-debug
    INSTALLED_APPS.append('template_debug')
    import django_extensions #django-extensions
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
    for d in ('./', './template_set', './_layouts', './_includes'):
        dd = os.path.join(PROJECT_ROOT_PATH, d)
        if os.path.exists(dd):
            DIR_TEMPLATES.append(dd)

DIR_TEMPLATES.append(DEFAULT_TEMPLATES)

TEMPLATES = [
    { 'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': DIR_TEMPLATES,
  },
]

MIDDLEWARE_CLASSES = []

add_to_builtins('actionkit_templates.templatetags.actionkit_tags')

def _is_static_context(request, args):
    return (re.search(r'wget', request.META.get('HTTP_USER_AGENT'), re.I)
            or args.get('contextdata')
            or os.environ.get('CONTEXTDATA', None))

def _get_context_data(request, name=None, page=None, use_referer=False):
    from actionkit_templates.contexts.page_contexts import contexts
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
    
    cxt = dict()
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

    static_data = _is_static_context(request, args)
    cxt['devenv'] = {
        'enabled': True,
        'port': port,
        'STATIC_URL': STATIC_URL,
        'STATIC_LOCAL': STATIC_LOCAL,
        'MO_EVENTS_API': './STATICDATA/context/',
        'useStaticData': static_data,
        # if you include a actionkit.forms.contextRoot = "{{devenv.contextRoot}}"
        # then this will be a page that can be saved statically and uniquely per-page
        # for e.g. static loading
        'contextRoot': './%s_STATIC_FAKE_DATA/context/' % page
    }
    if static_data:
        cxt['devenv']['contextData'] = _context_json(
            cxt,
            page,
            request.META.get('HTTP_REFERER') if use_referer else request.path
        )

    cxt['request'] = request
    cxt['js_context'] = '""' # FUTURE: what should go in here?
    return cxt

#############
# HOME PAGE TEST
#############

def index(request, name, page=None):
    cxt = _get_context_data(request, name, page)
    template = request.GET.get('template',
                               cxt.get('filename', "homepagetest.html"))

    return render_to_response(template, cxt)

def _context_json(cxt, page, coming_from, login_request=False):
    from actionkit_templates.contexts.event_context_json import event_json
    event_json_copy = event_json.copy()
    if cxt.get('user') and cxt.get('user').get('name'):
        event_json_copy.update(cxt['user'])
        if cxt.get('user_context'):
            event_json_copy.update(cxt['user_context'])
        if 'incomplete' in cxt:
            event_json_copy['incomplete'] = cxt['incomplete']
    if 'event' in coming_from \
       or 'logged_in' in coming_from \
       or (page and 'logged_in' in page):

        if not login_request \
              and 'logged_in' not in coming_from \
              and 'name' in event_json_copy \
              and (not page or 'logged_in' not in page):
            del event_json_copy['name']
        return json.dumps(event_json_copy)
    elif cxt.get('context'):
        return json.dumps(cxt['context'])
    else:
        #text key has all the generic error messages
        return '{"text": %s}' % json.dumps(event_json['text'])


def login_context(request, name=None, page=None, context=False, page_name=None):
    cxt = _get_context_data(request, name=name, page=page, use_referer=not context)
    coming_from = request.GET.get('url','')
    login_request = request.GET.get('login')
    context_json_str = _context_json(cxt, page, coming_from, login_request)
    return HttpResponse('actionkit.forms.onContextLoaded(%s)' % context_json_str)

def user_password_forgot(request):
    return HttpResponse('unimplemented')

def logout(request):
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect('/logout.html')

def event_search_results(request, page, name=None, context=False):
    cxt = _get_context_data(request, 'events', page, use_referer=not context)
    # special query results context:
    all = cxt['args'].get('all') == '1'
    cxt.update({'all': all})
    search_results = render_to_string('event_search_results.html', cxt)
    if _is_static_context(request, cxt['args']) and 'with_results' not in page:
        # static data should only be shown for results
        search_results = []
    if cxt.get('SLOW_SEARCH'):
        # This allows us to test for race conditions
        time.sleep(2)
    return HttpResponse('actionkit.forms.onEventSearchResults({})'
                        .format(json.dumps(search_results)))

def event_api_moveon_fake(request, name=None, page=None, fakeinfo=None):
    """Fake representation of MoveOn events api"""
    cxt = _get_context_data(request, 'events', page or 'WILL_USE_REFERER_HEADER', use_referer=not page)
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


#############
# URLS
#############

ROOT_URLCONF = 'actionkit_templates.settings'

urlpatterns = [
    url(r'^context', login_context),
    url(r'^progress', login_context, name='progress'),
    url(r'^logout', logout, name="logout"),
    ## _STATIC_FAKE_DATA endpoints are local instead of global and append _STATIC_FAKE_DATA to the page key
    ## This is all in-service of wget and the process to build static page versions that can easily be uploaded
    ## to S3.
    ## If more than three underscores are in a page key, then wget will not append ".html" inside the html CONTENT
    ## -- without the _(static)_(fake)_(data) underscores, local accesses
    ## It's also useful that the directory/path for this data is different than the file itself, to avoid file-system collisions
    ## We make it all local, so the results from this data can be particular to the page context test without
    ## depending on query strings which can't be used for static file responses
    url(r'^(?P<name>[-.\w]+)/(?P<page>[-.\w]+)/STATICDATA/context/fake-event-(?P<fakeinfo>titles|data).json$',
        event_api_moveon_fake, name="event_api_moveon_fake_local"
    ),
    url(r'^(?P<name>[-.\w]+)/(?P<page>[-.\w]+)_STATIC_FAKE_DATA/(context|progress)(/index.\w+)?/?(?P<page_name>[-.\w]+)?$',
        login_context, name="local_context",
        kwargs={'context': True}
    ),
    url(r'^(?P<name>[-.\w]+)/(?P<page>[-.\w]+)_STATIC_FAKE_DATA/cms/event/[-.\w]+/search_results(/index.\w+)?/?$',
        event_search_results, name="local_event_search_results",
        kwargs={'context': True}
    ),
    url(r'^(?P<name>[-.\w]+)?(/(?P<page>[-.\w]+))?(/page)?$', index),
    url(r'^forgot/$', user_password_forgot, name='user_password_forgot'),
    url(r'cms/event/(?P<page>[-.\w]+)/search_results/', event_search_results, name='event_search_results'),
    url(r'^fake/api/events', event_api_moveon_fake, name="event_api_moveon_fake"),
    # ActionKit urls or {% url %} template tag:
    url(r'^fake/stub/reverse', event_api_moveon_fake, name="reverse_donation"),
]
if STATIC_ROOT:
    urlpatterns = (urlpatterns
                   + static(STATIC_URL, document_root=STATIC_ROOT)
                   + static('/resources/',
                            view=proxy_serve,
                            document_root=os.path.join(STATIC_ROOT, './resources'))
                   + static('/media/',
                            view=proxy_serve,
                            document_root=os.path.join(STATIC_ROOT, './media'))
    )

if os.path.exists(os.path.join(PROJECT_ROOT_PATH, 'local_settings.py')):
    from local_settings import *
