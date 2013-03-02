"""Factories for the models of the ``people`` app."""
import factory

from django_libs.tests.factories import SimpleTranslationMixin

from ..models import (
    Link,
    LinkType,
    LinkTypeTranslation,
    Person,
    PersonPluginModel,
    PersonTranslation,
    Role,
    RoleTranslation,
)


class PersonFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for ``Person`` objects."""
    FACTORY_FOR = Person

    @staticmethod
    def _get_translation_factory_and_field():
        return (PersonTranslationFactory, 'person')


class PersonTranslationFactory(factory.Factory):
    """Factory for ``PersonTranslation`` objects."""
    FACTORY_FOR = PersonTranslation

    first_name = 'First name'
    person = factory.SubFactory(PersonFactory)
    language = 'en'


class PersonPluginModelFactory(factory.Factory):
    """Factory for ``PersonPluginModel`` objects."""
    FACTORY_FOR = PersonPluginModel

    display_type = 'small'
    person = factory.SubFactory(PersonFactory)


class RoleFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for ``Role`` objets."""
    FACTORY_FOR = Role

    @staticmethod
    def _get_translation_factory_and_field():
        return (RoleTranslationFactory, 'role')


class RoleTranslationFactory(factory.Factory):
    """Factory for ``RoleTranslation`` objects."""
    FACTORY_FOR = RoleTranslation

    name = factory.Sequence(lambda n: 'role {0}'.format(n))


class LinkTypeFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for ``LinkType`` objects."""
    FACTORY_FOR = LinkType

    @staticmethod
    def _get_translation_factory_and_field():
        return (LinkTypeTranslationFactory, 'link_type')


class LinkTypeTranslationFactory(factory.Factory):
    """Factory for ``LinkTypeTranslation`` objects."""
    FACTORY_FOR = LinkTypeTranslation

    name = factory.Sequence(lambda n: 'link type {0}'.format(n))
    link_type = factory.SubFactory(LinkType)
    language = 'en'


class LinkFactory(factory.Factory):
    """Factory for ``Link`` objects."""
    FACTORY_FOR = Link

    person = factory.SubFactory(PersonFactory)
    link_type = factory.SubFactory(LinkTypeFactory)
    url = 'www.example.com'
