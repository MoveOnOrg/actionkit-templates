ActionKit Template Renderer
===========================

### What this is

If you use [ActionKit](http://actionkit.com/) and edit its templates, then you might want to see what they look like
locally.  If you install this (`pip install actionkit-templates`) then you can run

```
aktemplateserve runserver
```

in a directory where you have a set of ActionKit templates (`wrapper.html`, etc), then you can 
view them on from a local port.  This runs Django in a similar environment that ActionKit
runs itself.


Environment
===========

You can set some environment variables that will help you develop locally (e.g. static file versions).

This is a 0.1 codebase, so things might change across versions -- probably limiting the full Django
manage.py context and to expose those things by commandline, instead.  In the meantime, you can
look at `actionkit_templates/settings.py` and search for `os.environ` for what it does.


Contributing When You Run Into Something Not Covered
====================================================

Template Tags
-------------

Usually, these are easy to add here `actionkit_templates/templatetags/actionkit_tags.py`
We should aim for support of all these:
  https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html

Extra contexts
--------------

If you make a context that's not covered already, please contribute with a patch to
`actionkit_templates/contexts/`  Note that these are also useful to browser, to see
what variables you can access from a particular page context.

