# How to setup automated tests

## Setting up tests will require a few things

1. Creating a `./tests/tests.py` file in your project
2. Automated testing will require a .travis.yml file and setting Travis-ci.com up.

## Creating a testing file

Create a file `./tests/tests.py` starting with the following content:

```
import re
import time

from actionkit_templates.test import TemplateTest

class TemplateTest(TemplateTest):

    def test_donate(self):
        self.open('/donations/donate.1?amounts=17-39-51-other')
        # test whether 'donation_type' text is present likely for choosing/setting the donation_type
        self.assertTrue(re.search(r'donation_type', self.wd.page_source))

```

## Setting things up to run tests locally

1. If you haven't already see the README for creating and installing this project in a python virtualenv,
and then make sure you run `pip install selenium==3.8.0 pyvirtualdisplay` for test dependencies

2. Then download the 'geckodriver' at [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases), and install it centrally (`/usr/local/bin` or `/usr/bin` -- somewhere in your path, so it appears when you run `which geckodriver`)

*If* you get an error when trying to run the tests, then upgrade selenium (probably to 3.8+) with `pip install -U selenium`.
The versions above are set to work with Travis

## Running tests

Tests are run with:

  aktemplates test tests

which runs the tests in `./tests/tests.py`. If you want to see the browser in linux go through the tests, then add:

  VISIBLE=1 aktemplates test tests

An experimental thing to test is run with

  SCREENSHOTS=1 aktemplates test tests

...which, in theory, will save screenshots from testing.

You can Also run individual tests.

## Adding tests

Create more tests by adding more `def test_....` functions. Use the test_donate() test method as a model.

Generally you want to first `self.open('/path/to_aktemplate_page')`, and then query and manipulate the page with
 `self.wd....` [selenium python functions](https://selenium-python.readthedocs.io/getting-started.html).

Finally, add some `self.assertTrue(...)`

Especially useful selenium wd methods and properties are:

* page_source (a string with the full source)
* find_element_by_name()
* find_element_by_id()
* ...


## Things to be mindful of when writing tests

* Note that aktemplates only simulates the rendering, so do not `submit()` a form.  Better to test the values and visibility of DOM elements and possibly javascript state.
* Use the existing contexts or make new ones in `./contexts.json`


## Automating Tests: Travis

This tutorial assumes Travis, but you can write something similar in most CLIs.

Create a `.travis.yml` with the following content:

```
language: python
python:
  - "2.7"

before_install:
  - wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
  - mkdir geckodriver
  - tar -xzf geckodriver-v0.19.1-linux64.tar.gz -C geckodriver
  - export PATH=$PATH:$PWD/geckodriver

install:
  - pip install selenium==3.8.0 pyvirtualdisplay -e git://github.com/MoveOnOrg/actionkit-templates#egg=actionkit-templates

before_script:
  - "export DISPLAY=:99.0"
  - "sh -e /etc/init.d/xvfb start"
  - sleep 3

script: aktemplates test tests
```

You'll likely want to put additional content on the bottom for automatic deploys or notifications.
See Travis documentation for that.


