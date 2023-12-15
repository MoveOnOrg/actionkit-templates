# Testing

## Install test dependencies

```
pip install ".[test]"
```

1. Creating a `./tests/tests.py` file in your project
2. Travis CI??
2. Then download the 'geckodriver' at [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases), and install it centrally (`/usr/local/bin` or `/usr/bin` -- somewhere in your path, so it appears when you run `which geckodriver`)


## Running tests

Tests are run with:

```
aktemplates test tests
```

If you want to see the browser in linux go through the tests, then add:

```
VISIBLE=1 aktemplates test tests
```

An experimental thing to test is run with

```
SCREENSHOTS=1 aktemplates test tests
```

...which, in theory, will save screenshots from testing.


## Adding tests

Create more tests by adding more `def test_....` functions. Use the test_donate() test method as a model.

Generally you want to first `self.open('/path/to_aktemplate_page')`, and then query and manipulate the page with `self.wd....` [selenium python functions](https://selenium-python.readthedocs.io/getting-started.html).

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
  - "3.10"

before_install:
  - wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
  - mkdir geckodriver
  - tar -xzf geckodriver-v0.19.1-linux64.tar.gz -C geckodriver
  - export PATH=$PATH:$PWD/geckodriver

install:
  - pip install selenium==3.8.0 pyvirtualdisplay dsa-actionkit

before_script:
  - "export DISPLAY=:99.0"
  - "sh -e /etc/init.d/xvfb start"
  - sleep 3

script: aktemplates test tests
```

You'll likely want to put additional content on the bottom for automatic deploys or notifications.
See Travis documentation for that.
