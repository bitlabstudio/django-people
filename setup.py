import os
from setuptools import setup, find_packages
import people as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-people",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, cms, plugin, people, person, profile',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-people",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'django-libs',
        'django-filer',
        'django-cms',
        'Pillow',
        'django-hvad',
        'django-localized-names',
    ],
)
