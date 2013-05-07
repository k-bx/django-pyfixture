from django.db.models import Model, CharField


class Foo(Model):
    name = CharField(max_length=20)
