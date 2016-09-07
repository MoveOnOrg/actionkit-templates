ActionKit Template Renderer
===========================

### What this is

If you use ActionKit and edit its templates, then you might want to see what they look like
locally.  If you install this (`pip install actionkit-templates`) then you can run

```
aktemplateserver runserver
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

