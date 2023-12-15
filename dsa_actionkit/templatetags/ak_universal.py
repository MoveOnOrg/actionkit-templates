"""
These tags seem to be available in base-line (i.e. all forms)
so we import register from defaulttags
"""

from django.conf import settings
from django.template.defaulttags import register

@register.filter
def single_line(value):
    "issue: this seems to be pre-loaded tag without actionkit_tags -- diff django version?"
    return value.replace('\n',' ')

@register.simple_tag
def client_name():
    "is this true?  that it's universally available?"
    return getattr(settings, 'AK_CLIENT_NAME', '--Site_ClientName--')

@register.simple_tag
def client_domain():
    return getattr(settings, 'AK_CLIENT_DOMAIN', 'actionkit.example.com')

