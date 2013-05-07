# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
# from django.core.management.base import CommandError
from django_pyfixture import load_py_fixtures_by_names


class Command(BaseCommand):
    """Command that gives you an ability to load fixtures written in python.

    Just put your fixtures into regular `app/fixtures/foo.py` file,
    then add them into `py_fixtures` list inside your test class.
    """
    args = '<fixture_name fixture_name ...>'
    help = 'Loads/executes py-fixtures'

    def handle(self, *args, **options):
        loaded = load_py_fixtures_by_names(args)
        if loaded:
            self.stdout.write(u'Successfully loaded "%s"\n' % ', '.join(loaded))
        else:
            self.stdout.write(u'No fixtures for "%s" found\n' % ', '.join(args))
