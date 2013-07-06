.. Django PyFixture documentation master file, created by
   sphinx-quickstart on Tue May  7 17:30:10 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django PyFixture's documentation!
============================================

..
   Contents:

   .. toctree::
      :maxdepth: 2

Resources
=========

- `Project on PyPi <https://pypi.python.org/pypi/django_pyfixture/>`_
- `Project on BitBucket <https://bitbucket.org/k_bx/django-pyfixture>`_
- `Mirror on github <https://github.com/k-bx/django-pyfixture>`_

Installation
============

1.  Add `django_pyfixture` into your `INSTALLED_APPS`.
2.  Create empty `<appname>/fixtures/__init__.py` file inside your
    django app called `<appname>`.
3.  Create your fixtures in files like `<appname>/fixtures/foo.py`
    with content similar to this:

.. code-block:: python

    # file proj/appname/fixtures/foo.py

    from django_pyfixture import PyFixtureBase


    class FooData(PyFixtureBase):
        def load_data(self):
            # create your python objects here
            pass

4.  Add inheritance into your base test class like this:


    .. warning::

       Make sure you put `PyFixtureTestCase` before
       `DjangoTestCase`. Seems that Unittest2-guys didn't inherit
       `object`, so now multi-inheritance via `super()` doesn't work
       good if order isn't right.

.. code-block:: python

    # file proj/utils/test_bases.py

    from django_pyfixture import PyFixtureTestCase
    from django.test import TestCase as DjangoTestCase


    class BaseTestCase(PyFixtureTestCase, DjangoTestCase):
        pass

5.  Add `py_fixtures` list inside your tests like this:

    .. code-block:: python

        # file proj/appname/tests/foo_tests.py

        class TestFoo(BaseTestCase):
            py_fixtures = ['foo']

            def test_should_get_list_of_foo(self):
                # do something with foo here
                Foo.objects.all()

6.  To load some data from terminal use

    .. code-block:: bash

        python manage.py loaddata_py foo

Additional info
===============

.. warning::

   Remember, there's no magical way to clean-up any side-effects you
   cause, so if you do something beyond transactions (like writing to
   redis) -- make sure you'll add cleanup after test or inside base
   test case. Cleanup method will be added into `django-pyfixture`
   later.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
