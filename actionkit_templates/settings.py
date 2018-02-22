import json
import os
import sys

from django.conf.urls import url
from django.conf.urls.static import static
from django.shortcuts import render_to_response

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

#############
# HOME PAGE TEST
#############

def index(request, name, page=None):
    from actionkit_templates.contexts.page_contexts import contexts
    port = '4000'
    hostport = request.get_host().split(':')
    if len(hostport) > 1:
        port = hostport[1]

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
        devenv={'enabled': True, 'port':port},
    )
    context_data = contexts.get(name,{})
    if page:
        context_data = contexts.get(name, {}).get(page, {})
    cxt.update(context_data)
    if not context_data:
        cxt.update({
            'page': {'title':'Homepage'},
            'pagelinks': sorted(contexts.items())})
    if request.GET.get('user_id'):
        #for debugging tests based on user.id % 2, e.g.
        context_data.setdefault('user', {}).update({'id': int(request.GET.get('user_id'))})

    template = request.GET.get('template',
                               context_data.get('filename', "homepagetest.html"))
    cxt.setdefault('args', {}).update(request.GET.dict())

    return render_to_response(template, cxt)

def login_context(request):
    import json
    from actionkit_templates.contexts.event_context_json import event_json
    from django.http import HttpResponse
    coming_from = request.GET.get('url','')
    if 'event' in coming_from \
       or 'logged_in' in coming_from:
        if not request.GET.get('login'):
            del event_json['name']
        return HttpResponse(
            'actionkit.forms.onContextLoaded(%s)' % json.dumps(event_json))
    else:
        return HttpResponse(
            #text key has all the generic error messages
            'actionkit.forms.onContextLoaded({"text": %s})' % json.dumps(event_json['text']))

def user_password_forgot(request):
    return HttpResponse('unimplemented')

#############
# STATIC DIRECTORY
#############

#note this only works if DEBUG=True
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(PROJECT_ROOT_PATH, './static'))
STATIC_URL = '/static/'
STATIC_FALLBACK = os.environ.get('STATIC_FALLBACK', False)

#############
# URLS
#############

ROOT_URLCONF = 'actionkit_templates.settings'

urlpatterns = [
    url(r'^context', login_context),
    url(r'^(?P<name>[-.\w]+)?(/(?P<page>[-.\w]+))?$', index),
    url(r'^forgot/$', user_password_forgot, name='user_password_forgot'),
    # ... the rest of your URLconf goes here ...
] + static(STATIC_URL, document_root=STATIC_ROOT)
