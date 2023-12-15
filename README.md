# ActionKit Template Renderer
---

## What this is

If you use [ActionKit](http://actionkit.com/) and edit its templates, then you might want to see what they look like
locally.

## Prerequisites

- Python < 3.12

## Quickstart

```console
$ mkdir myproject && cd myproject
$ python --version
Python 3.11.7
$ python -m venv .venv
$ source .venv/bin/activate
(myproject) $ pip install dsa-actionkit
(myproject) $ aktemplates runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 14, 2023 - 22:24:28
Django version 3.2.6, using settings 'dsa_actionkit.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Developing

Clone the repo and install the project package and all dependencies in editable mode:

  ```
  pip install -e .
  ```

## Customize

1. Put your actionkit templates in a directory called `template_set` (configurable)
2. Put your static assets (javascript, css) in a directory called `static` (configurable)

### Environment variables

You can customize your setup further by using environment variables:

`TEMPLATE_DIR`

By default we search the local directory and a directory called template_set.  If you run:

```
TEMPLATE_DIR=actionkittemplates aktemplates runserver
```

it will also look in the directory `actionkittemplates/`

`CUSTOM_CONTEXTS`

You can add additional test contexts and put them in either a file called `contexts.json` or set this environment variable to the json file to use.  JSON files should be in the form:

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

`STATIC_ROOT`

By default we serve the `./static/` directory at /static/  This goes well with code in your wrapper.html template like this:

```html
    {% if args.env == "dev" or devenv.enabled or 'devdevdev' in page.custom_fields.layout_options %}
      <!-- development of stylesheets locally -->
      <link href="/static/stylesheets/site.css" rel="stylesheet" />
    {% else %}
      <!-- production location of stylesheets -->
      <link href="https://EXAMPLE.COM/static/stylesheets/site.css" rel="stylesheet" />
    {% endif %}
```

`STATIC_FALLBACK`

In the occasional moment when you are developing without an internet connection this will fail to load:

```
{% load_js %}
//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js
{% end %}
```

In that situation, if you set STATIC_FALLBACK to a directory where, e.g. `jquery.min.js` is present, then it will look for all the internet-external files in that directory. Note that this only works with `load_js` and `load_css` template tags.

Adding Tests
============

See documentation in [TESTING.md](./TESTING.md)

Template Tags
-------------

Usually, these are easy to add here [dsa_actionkit/templatetags/actionkit_tags.py](https://github.com/dsa-ntc/actionkit-templates/blob/master/dsa_actionkit/templatetags/actionkit_tags.py) Actionkit provides implementations [here](https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html)

Extra contexts
--------------

If you make a context that's not covered already, please contribute with a patch to
[dsa_actionkit/contexts/](https://github.com/dsa-ntc/actionkit-templates/tree/master/dsa_actionkit/contexts) Note that these are also useful to browse to see
what variables you can access from a particular page context.
