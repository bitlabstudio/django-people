"""Factories for the models of the ``people`` app."""
from django.conf import settings

import factory
from django_libs.tests.factories import HvadFactoryMixin

from ..models import (
    Nationality,
    Link,
    LinkType,
    Person,
    PersonPluginModel,
    Role,
)


class NationalityFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``Nationality`` model."""
    FACTORY_FOR = Nationality

    name = factory.Sequence(lambda n: 'nationality {0}'.format(n))


class PersonFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for ``Person`` objects."""
    FACTORY_FOR = Person

    roman_first_name = 'First name'
    language_code = settings.LANGUAGE_CODE


class PersonPluginModelFactory(factory.DjangoModelFactory):
    """Factory for ``PersonPluginModel`` objects."""
    FACTORY_FOR = PersonPluginModel

    display_type = 'small'
    person = factory.SubFactory(PersonFactory)


class RoleFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for ``Role`` objets."""
    FACTORY_FOR = Role

    name = factory.Sequence(lambda n: 'role {0}'.format(n))


class LinkTypeFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for ``LinkType`` objects."""
    FACTORY_FOR = LinkType

    name = factory.Sequence(lambda n: 'link type {0}'.format(n))


class LinkFactory(factory.DjangoModelFactory):
    """Factory for ``Link`` objects."""
    FACTORY_FOR = Link

    person = factory.SubFactory(PersonFactory)
    link_type = factory.SubFactory(LinkTypeFactory)
    url = 'www.example.com'
