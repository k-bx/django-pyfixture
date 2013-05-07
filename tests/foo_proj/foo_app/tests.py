# -*- coding: utf-8 -*-

from foo_app.utils import BaseTestCase


class TestIndex(BaseTestCase):
    py_fixtures = ['foo']

    def test_should_check_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            "Hello, world! Foo names are: bar, baz, foo!")


class TestIndexNoFixtures(BaseTestCase):
    def test_should_get_empty_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            "Hello, world! Foo names are: !")
