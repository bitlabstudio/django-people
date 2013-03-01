Django People
=============

A simple app to show person profiles, for example for the "About us" section
of a website.

Comes with a django-cms plugin and is multilingual.

Prerequisites
-------------

You will need to have the following packages installed:

* Django
* django-cms (optional)
* django-filer
* simple-translation
* Pillow
* South


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install django-people

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-people.git#egg=people

Add ``people`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'people',
    )

Run the South migrations::

    ./manage.py migrate people 


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
