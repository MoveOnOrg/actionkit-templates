import datetime
import os
import re
from django.conf import settings
from django.template import loader, Library, Node, Variable
from django.template.base import Context
from django.template.defaultfilters import safe
from django.utils import timezone
from django.utils.html import strip_tags

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

class OnceNode(Node):
    rendered = False

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        if not self.rendered:
            self.rendered = True
            return self.nodelist.render(context)
        else:
            return ''

class SetVarNode(Node):
    var_name = "now"

    def render(self, context):
        context[self.var_name] = datetime.datetime.now(timezone.utc)
        return ''


class RecordNode(Node):
    def __init__(self, item, ary, reportresult=False):
        self.item = Variable(item)
        self.ary = Variable(ary)
        self.reportresult = reportresult

    def render(self, context):
        ary = self.ary.resolve(context)
        if not ary:
            context[self.ary] = []
        item = self.item.resolve(context)
        if self.reportresult:
            found = re.search(r'\d+', str(item))
            if found:
                item = int(found.group(1))
        ary.append(item)
        return ''

@register.tag
def once(parser, token):
    """
    Use the tag once to wrap template code that will only be rendered one time.
    """
    nodelist = parser.parse(('endonce',))
    parser.delete_first_token()
    return OnceNode(nodelist)

@register.tag
def record(parser, token):
    """
    https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html#record
    {% with "[ ]"|load_json as user_quiz_score %}
      {% for field in action.custom_fields %}
        {% if field == [THE RIGHT ANSWER FOR THIS QUESTION] %}
          {% record 1 in user_quiz_score %}
        {% endif %}
      {% endfor %}
      Your final score was {{ user_quiz_score|length }}
    {% endwith %}
    """
    reportresult = False
    tokens = token.split_contents()
    if tokens[0] == 'reportresult':
        reportresult = True
        tokens = tokens[1:]
    return RecordNode(item=tokens[1], ary=tokens[3], reportresult=reportresult)

@register.tag
def right_now(parser, token):
    """
    The tag right_now creates the variable {{ now }}
    that contains the Python datetime object datetime.now().
    """
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
def load_ak_context(somestring, *args, **kwargs):
    return ''

@register.simple_tag
def braintree_js_libs():
    return '''
    <script src="https://js.braintreegateway.com/web/3.27.0/js/client.min.js"></script>
    <script src="https://js.braintreegateway.com/web/3.27.0/js/hosted-fields.min.js"></script>
    <script src="https://js.braintreegateway.com/web/3.27.0/js/data-collector.min.js"></script>
    <script src="https://js.braintreegateway.com/web/3.27.0/js/us-bank-account.min.js"></script>
    '''

@register.simple_tag
def authnet_js_libs():
    return '''
    <script type="text/javascript" src="https://jstest.authorize.net/v1/Accept.js" charset="utf-8">
    </script>
    '''

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
    """
    Return an absolute <link rel=stylesheet>
    for each non-empty line in the block, e.g.

    {% load_css %}
    https://example.com/mystyles.css
    //example.com/morestyles.css
    /static/yetmorestyles.css
    https://fonts.googleapis.com/css?family=Open+Sans:100,300,400,600,700

    {% end %}

    should render

    <link rel="stylesheet" href="https://example.com/mystyles.css" />
    <link rel="stylesheet" href="https://mydomain.actionkit.com/example.com/morestyles.css" />
    <link rel="stylesheet" href="https:///static/yetmorestyles.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:100,300,400,600,700" />
    """

    nodelist = parser.parse(('end',))
    parser.delete_first_token()
    source = nodelist[0].s
    parsed = ''.join([
        """<link rel="stylesheet" href="%s" />""" % _add_domain(s.strip())
        for s in source.strip().splitlines()
        if s and s.strip()
    ])
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
def split(value, arg=' '):
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
def get(value, arg):
    return value[arg]

@register.filter
def mod(value, arg):
    return int(value or 0) % int(arg)

@register.filter
def add(value, arg):
    value_mod = int(value) if int(float(value)) == float(value) else float(value)
    arg_mod = int(arg) if int(float(arg)) == float(arg) else float(arg)
    return value_mod + arg_mod

@register.filter
def subtract(value, arg):
    return float(value) - float(arg)

@register.filter
def date_add(value, arg):
    # https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html#date-add
    kwargs = {}
    args = arg.split(' ')
    for a in args:
        if '=' in a:
            k, val = a.split('=')
            if k and val:
                kwargs[k] = int(val)
    return value + datetime.timedelta(**kwargs)

@register.filter
def multiply(value, arg):
    value_mod = int(value) if int(float(value)) == float(value) else float(value)
    arg_mod = int(arg) if int(float(arg)) == float(arg) else float(arg)
    return value_mod * arg_mod

@register.filter
def percent_of(value, arg):
    return '%.1f' % (100 * (float(value) / float(arg)))

@register.filter
def get_fields(obj):
    return [(i, obj[i]) for i in obj]
    # return [(field.name, field.value_to_string(obj)) for field in obj._meta.fields]

@register.simple_tag
def authnet_js_libs():
    return ''

@register.simple_tag
def braintree_js_libs():
    return ''

@register.simple_tag
def client_domain_url(path):
    return '%s/%s' % (client_domain(), path)

@register.simple_tag
def divide(top, bottom, precision):
    return '%.{}f'.format(precision) % (float(top)/float(bottom))

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
    try:
        return format(int(value), ",d")
    except ValueError:
        if isinstance(value, float):
            value = str(value)
        parts = value.split('.')
        return '{}.{}'.format(format(int(parts[0]), ",d"), parts[1])

@register.filter
def concatenate(value, arg):
    "add commas for numeric values"
    return '{}{}'.format(value, arg)

@register.filter
def custom_hash(value):
    "This creates a custom akid generation"
    return '{}.{}'.format(value, 'fakehash')

@register.filter
def is_defined(value):
    return bool(value)

@register.filter
def is_nonblank(value):
    """
    The filter is_nonblank returns True if the string does not appear blank
    when rendered - that is, it consists of more than just whitespace and invisible HTML.

    For example the strings with spaces and \t , and &nbsp; ,
    and <p></p><div class="lol">&nbsp;</div> would all return False.
    """
    if value:
        return bool(re.sub(r'\s', '', strip_tags(value).replace('&nbsp;','')))
    return False

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
    """
    First replace multiple newlines with a single newline,
    then collapse multiple non-newline whitespace characters
    """
    return re.sub(r'(?![\r\n])\s+', ' ', re.sub(r'[\r\n]+', '\n', value))

@register.filter
def get(value, key):
    if hasattr(value, 'get'):
        return value.get(key)
    elif hasattr(value, key):
        return getattr(value, key)

@register.filter
def matches(value, regex):
    return bool(re.search(regex, value))

@register.filter
def strip_nondigits(value):
    return re.sub(r'\D', '', value)

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
