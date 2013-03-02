"""Tests for the models of the ``people`` app."""
from django.test import TestCase

from .factories import (
    LinkFactory,
    LinkTypeFactory,
    PersonFactory,
    PersonPluginModelFactory,
    RoleFactory,
)


class LinkTestCase(TestCase):
    """Tests for the ``Link`` model."""
    longMessage = True

    def test_model(self):
        obj = LinkFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))


class LinkTypeTestCase(TestCase):
    """Tests for the ``LinkType`` model."""
    longMessage = True

    def test_model(self):
        obj = LinkTypeFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))


class PersonTestCase(TestCase):
    """Tests for the ``Person`` model."""
    longMessage = True

    def test_model(self):
        obj = PersonFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))


class PersonPluginModelTestCase(TestCase):
    """Tests for the ``PersonPluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = PersonPluginModelFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_copy_relations(self):
        old_obj = PersonPluginModelFactory()
        new_obj = PersonPluginModelFactory()
        new_obj.copy_relations(old_obj)
        self.assertEqual(new_obj.person, old_obj.person, msg=(
            'Should copy the person instance from the old object to the new'
            ' object.'))


class RoleTestCase(TestCase):
    """Tests for the ``Role`` model."""
    longMessage = True

    def test_model(self):
        obj = RoleFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))
