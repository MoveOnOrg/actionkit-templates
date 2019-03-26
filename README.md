ActionKit Template Renderer
===========================

### What this is

If you use [ActionKit](http://actionkit.com/) and edit its templates, then you might want to see what they look like
locally.  If you install this (`pip install actionkit-templates`) then first setup your content:

1. Put your actionkit templates in a directory called `template_set` (configurable)
2. Put your static assets (javascript, css) in a directory called `static` (configurable)
3. Now run:

   aktemplates runserver

You can also run it on a different port than the default like so:

   aktemplates runserver 0.0.0.0:1234

in a directory where you have a set of ActionKit templates (`wrapper.html`, etc), then you can 
view them on from a local port.  This runs Django in a similar environment that ActionKit
runs itself.

Installation
============

The code is available from https://github.com/MoveOnOrg/actionkit-templates
If you have python's pip program installed, you can just run (possibly in a virtualenv):

   pip install -e git://github.com/MoveOnOrg/actionkit-templates#egg=actionkit-templates

Please note that this package installs the version of Django used on ActionKit production,
so use a virtualenv if you develop using Django on your computer so it doesn't change your local version.

For testing, you will also want to run:

   pip install selenium==3.8.0 pyvirtualdisplay

Environment
===========

You can set some environment variables that will help you develop locally (e.g. static file versions).

This is a 0.1 codebase, so things might change across versions -- probably limiting the full Django
manage.py context and to expose those things by commandline, instead.  In the meantime, you can
look at `actionkit_templates/settings.py` and search for `os.environ` for what it does.

TEMPLATE_DIR
: By default we search the local directory and a directory called template_set.  If you run:

    TEMPLATE_DIR=actionkittemplates aktemplates runserver

  it will also look in the directory `actionkittemplates/`

CUSTOM_CONTEXTS
: You can add additional test contexts and put them in either a file called `contexts.json` or
  set this environment variable to the json file to use.  JSON files should be in the form:

```json

   {"name_of_context": {
       "filename": "event_attend.html",
       "all_the_context_keys_for_this_context": {
       },
       "page": {
          "title": "My Page Title",
          "type": "Event"
       },
       "event": {
           "...": "..."
       }
   }

```

STATIC_ROOT
: By default we serve the `./static/` directory at /static/  This goes well with code in your
  wrapper.html template like this:
```
    {% if args.env == "dev" or devenv.enabled or 'devdevdev' in page.custom_fields.layout_options %}
      <!-- development of stylesheets locally -->
      <link href="/static/stylesheets/site.css" rel="stylesheet" />
    {% else %}
      <!-- production location of stylesheets -->
      <link href="https://EXAMPLE.COM/static/stylesheets/site.css" rel="stylesheet" />
    {% endif %}
```

STATIC_FALLBACK
: In the occasional moment when you are developing without an internet connection this will fail
  to load:

  ```
  {% load_js %}
  //ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js
  {% end %}
  ```

  In that situation, if you set STATIC_FALLBACK to a directory where, e.g. `jquery.min.js`
  is present, then it will look for all the internet-external files in that directory.
  Note that this only works with `load_js` and `load_css` template tags.


Adding Tests
============

See our documentation in [TESTING.md](./TESTING.md)

Contributing When You Run Into Something Not Covered
====================================================

Template Tags
-------------

Usually, these are easy to add here [actionkit_templates/templatetags/actionkit_tags.py](https://github.com/MoveOnOrg/actionkit-templates/blob/master/actionkit_templates/templatetags/actionkit_tags.py)
We should aim for support of all these:
  https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html

Extra contexts
--------------

If you make a context that's not covered already, please contribute with a patch to
[actionkit_templates/contexts/](https://github.com/MoveOnOrg/actionkit-templates/tree/master/actionkit_templates/contexts)
Note that these are also useful to browse, to see
what variables you can access from a particular page context.

License (MIT)
-------------

Copyright MoveOn.org written by Schuyler Duveen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.