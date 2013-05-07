#### Setup

from django.conf import settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF='foo',
        TEMPLATE_DIRS=['.'],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/tmp/django_pyfixture.sqlite3'}},
        INSTALLED_APPS=('foo_app',))

from django.conf.urls import patterns
urlpatterns = patterns(
    '',
    (r'^$', 'foo.index'),
)

#### Handlers

from django.http import HttpResponse
from foo_app.models import Foo


def index(request):
    foos = Foo.objects.all()
    foo_names = sorted([x.name for x in foos])
    foo_names_str = ", ".join(foo_names)
    return HttpResponse(
        "Hello, world! Foo names are: {}!".format(foo_names_str))

#### Running

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line()
