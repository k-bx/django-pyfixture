# -*- coding: utf-8 -*-

from django_pyfixture import PyFixtureBase

from foo_app.models import Foo


class FooData(PyFixtureBase):
    def load_data(self):
        Foo(name="foo").save()
        Foo(name="bar").save()
        Foo(name="baz").save()
