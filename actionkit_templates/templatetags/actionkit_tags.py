import datetime
import os
import re
from django.template import loader, Library, Node
from django.template.defaultfilters import safe
from django.conf import settings

"""
These are stub functions to avoid getting in the way of not having actionkit running.

Maybe in the future we would re-create these or at least make better stub values.

If you ever get an error of 'Invalid filter' or 'Invalid tag', you'll need to
add one below.  Take a look at:
https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
to figure out how to do the least work.

"""

register = Library()

class NoContentNode(Node):
    def render(self, context):
        return ''


class StaticContentNode(Node):
    def __init__(self, staticcontent):
        self.staticcontent = staticcontent

    def render(self, context):
        return self.staticcontent


class SetVarNode(Node):
    var_name = "now"
    
    def render(self, context):
        context[self.var_name] = datetime.datetime.now()
        return ''


@register.tag
def right_now(parser, token):
    "undocumented AK tag that creates a {{now}} variable"
    return SetVarNode()

@register.simple_tag
def client_name():
    return getattr(settings, 'AK_CLIENT_NAME', '--AK ClientName--')

@register.simple_tag
def facebook_app():
    return getattr(settings, 'AK_FACEBOOK_APP', '--facebook appid!--')

@register.simple_tag
def client_domain():
    return getattr(settings, 'AK_CLIENT_DOMAIN', 'roboticdogs.actionkit.com')

@register.simple_tag
def include_tmpl(field, *args):
    return safe('%s' % field)

@register.simple_tag
def url(lookup):
    #override default django url
    return '/someurl/blah/%s' % lookup


@register.simple_tag
def load_ak_context(somestring, *args, **kwargs):
    return ''

@register.tag
def field_order(parser, token):
    "takes a set of fields and sets the order for the form"
    return NoContentNode()

@register.tag
def hide_by_default(parser, token):
    "seems to take a field list and default-hides them"
    return NoContentNode()


def _add_domain(path):
    fallback = getattr(settings, 'STATIC_FALLBACK', False)
    filename = path.rsplit('/', 1)[1]
    if fallback:
        return '%s/%s' % (fallback, filename)
    elif path.startswith('//') or path.startswith('http'):
        return path
    return 'https://%s%s' % (client_domain(), path)


@register.tag
def load_css(parser, token):
    nodelist = parser.parse(('end',))
    parser.delete_first_token()
    source = nodelist[0].s
    parsed = ''.join(["""
    <link rel="stylesheet" href="%s" />
    """ % _add_domain(s)
        for s in re.findall(r'/[^\s]+css', source)])
    return StaticContentNode(parsed)

@register.tag
def load_js(parser, token):
    nodelist = parser.parse(('end',))
    parser.delete_first_token()
    source = nodelist[0].s
    parsed = ''.join(["""
    <script src="%s" ></script>
    """ % _add_domain(s)
        for s in re.findall(r'[^\s]+js', source)])
    return StaticContentNode(parsed)

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def truncateletters(value, arg):
    return value[:arg]

@register.filter
def is_in(value, arg):
    return arg in value

@register.filter
def nth(value, arg):
    return value[arg]

@register.filter
def mod(value, arg):
    return int(value) % int(arg)

@register.filter
def escapeall(value):
    return value

@register.filter
def json(value):
    import json as jjson
    return jjson.dumps(jjson.loads(value))

@register.filter
def load_json(value):
    import json as jjson
    return jjson.loads(value)

@register.filter
def ak_field_label(value, arg):
    return '%s|%s|' % (arg, value)

@register.filter
def tag_links(value, arg):
    """
    {% filter referring_akid:akid|tag_links:"source=taf" %}{% include_tmpl page.followup.taf_body escaped %}{% endfilter %}
    """
    # this hackily doesn't try to do good things with a pre-existing "?" in the url
    return re.sub(r'https?://[^"\'() ]+', '\1?%s' % arg, value)

@register.filter
def commify(value):
    "add commas for numeric values"
    return format(int(value), ",d")

@register.filter
def concatenate(value, arg):
    "add commas for numeric values"
    return '{}{}'.format(value, arg)

@register.filter
def is_defined(value):
    return bool(value)

@register.filter
def strip(value):
    return value.strip()

@register.filter
def columns(value, cols):
    "{% for row in amounts|columns:3 %}"
    vlen = len(value)
    return [ [value[i] for i in range(x,vlen,cols)]
             for x in range(cols)]

@register.filter
def referring_akid(value, akid):
    """
    example:{% filter referring_akid:akid|tag_links:"source=taf" %}{% include_tmpl page.followup.taf_body escaped %}{% endfilter %}
    """
    return value

@register.filter
def collapse_spaces(value):
    return re.sub(r'\s+', ' ', value)

@register.filter
def remove_blank_lines(value):
    return re.sub(r'\n\s*\n', '\n', value)

@register.filter
def is_nonblank(value):
    return value != ''

@register.filter
def ak_text(value, arg):
    """e.g. 
     <meta content="{% filter ak_text:"org_name" %}{% client_name %}{% endfilter %}">
    {% filter ak_text:"notaf_thanks_banner" %}
    {% filter ak_text:"taf_ask" %}{% endfilter %}
    """
    #this would be overridden by some variable if it existed in the instance
    return value
