# -*- coding: utf-8 -*-

from django_pyfixture import PyFixtureTestCase
from django.test import TestCase as DjangoTestCase


class BaseTestCase(DjangoTestCase, PyFixtureTestCase):
    pass
