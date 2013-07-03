"""Tests for the models of the ``people`` app."""
from django.test import TestCase

from .factories import (
    NationalityFactory,
    LinkFactory,
    LinkTypeFactory,
    PersonFactory,
    PersonPluginModelFactory,
    PersonTranslationFactory,
    RoleFactory,
)


class NationalityTestCase(TestCase):
    """Tests for the ``Nationality`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``Nationality`` model."""
        nationality = NationalityFactory()
        self.assertTrue(nationality.pk)
        # also test the instantiation of the NationalityTranslation
        self.assertTrue(nationality.get_translation().pk)


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


class PersonTranslationTestCase(TestCase):
    """Tests for the ``PersonTranslation`` model."""
    longMessage = True

    def setUp(self):
        self.obj = PersonTranslationFactory(
            person__roman_first_name='roman_first_name',
            person__roman_last_name='roman_last_name',
            person__non_roman_first_name='roman_first_name',
            person__non_roman_last_name='roman_last_name',
            person__title='Mr',
            person__chosen_name='nickname',
            person__gender='male',
        )

    def test_model(self):
        """Test instantiation of the PersonTranslation`` model."""
        self.assertTrue(self.obj.pk, msg=(
            'Should be able to instantiate and save the model.'))

    def test_localized_names_methods(self):
        """Tests for the interface methods for the ``localized_names`` app."""
        self.assertEqual(
            self.obj.get_romanized_first_name(),
            self.obj.person.roman_first_name,
            msg='Got the wrong roman first name.')
        self.assertEqual(
            self.obj.get_romanized_last_name(),
            self.obj.person.roman_last_name,
            msg='Got the wrong roman last name.')
        self.assertEqual(
            self.obj.get_non_romanized_first_name(),
            self.obj.person.non_roman_first_name,
            msg='Got the wrong non roman first name.')
        self.assertEqual(
            self.obj.get_non_romanized_last_name(),
            self.obj.person.non_roman_last_name,
            msg='Got the wrong non roman last name.')
        self.assertEqual(
            self.obj.get_title(),
            self.obj.person.title,
            msg='Got the wrong title.')
        self.assertEqual(
            self.obj.get_nickname(),
            self.obj.person.chosen_name,
            msg='Got the wrong nickname.')

    def test_get_gender(self):
        self.assertEqual(self.obj.get_gender(), 'Mr')

        self.obj.person.gender = 'female'
        self.obj.person.save()
        self.assertEqual(self.obj.get_gender(), 'Ms')

        self.obj.person.gender = ''
        self.obj.person.save()
        self.assertEqual(self.obj.get_gender(), '')


class RoleTestCase(TestCase):
    """Tests for the ``Role`` model."""
    longMessage = True

    def test_model(self):
        obj = RoleFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))
