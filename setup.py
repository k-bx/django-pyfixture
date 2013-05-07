from setuptools import setup

from django_pyfixture import __version__


setup(name='django_pyfixture',
      version=__version__,
      description='Django-PyFixture lets you write fixtures as regular .py-files.',
      url='https://bitbucket.org/k_bx/django-pyfixture',
      author='Konstantine Rybnikov',
      author_email='k-bx@k-bx.com',
      license='BSD',
      packages=['django_pyfixture'],
      zip_safe=False)
