==================
 Django PyFixture
==================

This package lets you write fixtures as regular `.py`-files.

Installation
============

1.  Add `django_pyfixture` into your `INSTALLED_APPS`.
2.  Create empty `<appname>/fixtures/__init__.py` file inside your
    django app called `<appname>`.
3.  Create your fixtures inside `fixtures` directory as a regular
    `foo.py` file.
4.  Put content inside that file that looks like this:

.. code-block:: python

    # file proj/appname/fixtures/foo.py

    from django_pyfixture import PyFixtureBase

    class FooData(PyFixtureBase):
        def load_data(self):
            # create your python objects here
            pass

5.  Add inheritance into your base test class like this:

.. code-block:: python

    # file proj/utils/test_bases.py

    from django_pyfixture import PyFixtureTestCase
    from django.test import TestCase as DjangoTestCase


    class BaseTestCase(DjangoTestCase, PyFixtureTestCase)

6.  Add `py_fixtures` list inside your tests like this:

.. code-block:: python

    # file proj/appname/tests/foo_tests.py

    class TestFoo(BaseTestCase):
        py_fixtures = ['foo']

        def test_should_get_list_of_foo(self):
            # do something with foo here
            Foo.objects.all()
