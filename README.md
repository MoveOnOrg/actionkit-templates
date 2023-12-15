# ActionKit Template Renderer
---

## What this is

If you use [ActionKit](http://actionkit.com/) and edit its templates, then you might want to see what they look like
locally.

## Prerequisites

Python & Docker

## Install Dependencies

1. Create and activate a virtual environment (optional, encouraged):

  - Unix (macOS, Linux (including WSL)):

    ```shell
    python -m venv .venv
    source .venv/bin/activate
    ```

  - Windows + Powershell:

    ```pwsh
    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

  2. Install Python packages with pip:

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

## Usage

Run:

  ```
  aktemplates runserver
  ```


You can also run it on a different port than the default like so:

   aktemplates runserver 0.0.0.0:1234

in a directory where you have a set of ActionKit templates (`wrapper.html`, etc), then you can
view them on from a local port.  This runs Django in a similar environment that ActionKit
runs itself.



Adding Tests
============

See documentation in [TESTING.md](./TESTING.md)

Template Tags
-------------

Usually, these are easy to add here [actionkit_templates/templatetags/actionkit_tags.py](https://github.com/dsa-ntc/actionkit-templates/blob/master/actionkit_templates/templatetags/actionkit_tags.py) Actionkit provides implementations [here](https://roboticdogs.actionkit.com/docs/manual/guide/customtags.html)

Extra contexts
--------------

If you make a context that's not covered already, please contribute with a patch to
[actionkit_templates/contexts/](https://github.com/MoveOnOrg/actionkit-templates/tree/master/actionkit_templates/contexts) Note that these are also useful to browse to see
what variables you can access from a particular page context.
