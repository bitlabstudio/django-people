Django People
=============

A simple app to show person profiles, for example for the "About us" section
of a website.

Comes with a django-cms plugin and is multilingual.


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install django-people

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-people.git#egg=people

Add ``people`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'cms',
        'menus',
        'treebeard',
        'filer',
        'easy_thumbnails',
        'people',
    )

Run the migrations::

    ./manage.py migrate people


Usage
-----

Use the Django admin to create your person objects. If you are using django-cms
you can use the ``Person Plugin`` to display a person in your placeholders.


Settings
--------

PERSON_PLUGIN_DISPLAY_TYPE_CHOICES
++++++++++++++++++++++++++++++++++

Default::

    [
        ('small', _('small')),
        ('big', _('big')),
    ]

When using the ``Person Plugin`` in your django-cms placeholders you will
notice that you only have two choices for the ``Display type``. This field
can be helpful when you want to render a person differently in different parts
of your site. If you need even more display types, just set this setting to
a different list of tuples.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
