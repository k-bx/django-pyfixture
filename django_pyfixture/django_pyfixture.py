# -*- coding: utf-8 -*-

from importlib import import_module
from inspect import getmembers
from inspect import isclass

from django.conf import settings

__version__ = '0.0.1'


class PyFixtureBase(object):
    def load_data(self):
        raise NotImplementedError


class PyFixtureTestCase(object):
    """Mixin for your base test case."""

    def setUp(self):
        super(PyFixtureTestCase, self).setUp()

    def tearDown(self):
        super(PyFixtureTestCase, self).tearDown()


def load_py_fixtures_from_test_case(test_case):
    if hasattr(test_case, 'py_fixtures'):
        if len(test_case.py_fixtures):
            load_py_fixtures_by_names(test_case.py_fixtures)


def load_py_fixtures_by_names(fixture_names):
    """Do the actual loading work."""
    # import logging

    loaded = []
    for fixture_name in fixture_names:
        fixture_classes = list(find_fixture_classes(fixture_name))
        # logging.debug(u"Loading fixture: %s" % fixture_name)
        for fixture_class in fixture_classes:
            # fire
            # logging.debug(u"- loading func %s" % fixture_class.__name__)
            fixture = fixture_class()
            fixture.load_data()
            loaded.append(fixture_name)
    return loaded


def find_fixture_classes(fixture_name):
    installed_apps = settings.INSTALLED_APPS
    for app_name in installed_apps:
        try:
            fixture_module_name = app_name + '.fixtures.' + fixture_name
            fixture_module = import_module(fixture_module_name)
            for member_name, member in getmembers(fixture_module):
                if (isclass(member)
                    and issubclass(member, PyFixtureBase)
                    and member is not PyFixtureBase):
                    #
                    yield member
        except ImportError:
            pass
