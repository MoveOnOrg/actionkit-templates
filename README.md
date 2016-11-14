ActionKit Template Renderer
===========================

### What this is

If you use [ActionKit](http://actionkit.com/) and edit its templates, then you might want to see what they look like
locally.  If you install this (`pip install actionkit-templates`) then you can run

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

   pip install actionkit-templates

Please note that this package requires the version of Django used on ActionKit production,
so use a virtualenv if you develop using Django on your computer so it doesn't change your local version.

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

License
-------

Copyright MoveOn.org written by Schuyler Duveen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
