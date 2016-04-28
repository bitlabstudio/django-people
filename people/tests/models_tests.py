"""Tests for the models of the ``people`` app."""
from django.test import TestCase

from mixer.backend.django import mixer


class NationalityTestCase(TestCase):
    """Tests for the ``Nationality`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``Nationality`` model."""
        nationality = mixer.blend('people.NationalityTranslation')
        self.assertTrue(str(nationality))


class LinkTestCase(TestCase):
    """Tests for the ``Link`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('people.Link')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))


class LinkTypeTestCase(TestCase):
    """Tests for the ``LinkType`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('people.LinkTypeTranslation')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))


class PersonTestCase(TestCase):
    """Tests for the ``Person`` model."""
    longMessage = True

    def setUp(self):
        self.obj = mixer.blend(
            'people.Person',
            roman_first_name='roman_first_name',
            roman_last_name='roman_last_name',
            non_roman_first_name='roman_first_name',
            non_roman_last_name='roman_last_name',
            title='Mr',
            chosen_name='nickname',
            gender='male',
        )
        self.obj.translate('en')

    def test_model(self):
        self.assertTrue(str(self.obj), msg=(
            'Should be able to instantiate and save the model.'))

    def test_localized_names_methods(self):
        """Tests for the interface methods for the ``localized_names`` app."""
        self.assertEqual(
            self.obj.get_romanized_first_name(),
            self.obj.roman_first_name,
            msg='Got the wrong roman first name.')
        self.assertEqual(
            self.obj.get_romanized_last_name(),
            self.obj.roman_last_name,
            msg='Got the wrong roman last name.')
        self.assertEqual(
            self.obj.get_non_romanized_first_name(),
            self.obj.non_roman_first_name,
            msg='Got the wrong non roman first name.')
        self.assertEqual(
            self.obj.get_non_romanized_last_name(),
            self.obj.non_roman_last_name,
            msg='Got the wrong non roman last name.')
        self.assertEqual(
            self.obj.get_title(),
            self.obj.title,
            msg='Got the wrong title.')
        self.assertEqual(
            self.obj.get_nickname(),
            self.obj.chosen_name,
            msg='Got the wrong nickname.')

    def test_get_gender(self):
        self.assertEqual(self.obj.get_gender(), 'Mr')

        self.obj.gender = 'female'
        self.obj.save()
        self.assertEqual(self.obj.get_gender(), 'Ms')

        self.obj.gender = ''
        self.obj.save()
        self.assertEqual(self.obj.get_gender(), '')


class PersonPluginModelTestCase(TestCase):
    """Tests for the ``PersonPluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('people.PersonPluginModel')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))

    def test_copy_relations(self):
        old_obj = mixer.blend('people.PersonPluginModel')
        new_obj = mixer.blend('people.PersonPluginModel')
        new_obj.copy_relations(old_obj)
        self.assertEqual(new_obj.person, old_obj.person, msg=(
            'Should copy the person instance from the old object to the new'
            ' object.'))


class RoleTestCase(TestCase):
    """Tests for the ``Role`` model."""
    longMessage = True

    def test_model(self):
        obj = mixer.blend('people.RoleTranslation')
        self.assertTrue(str(obj), msg=(
            'Should be able to instantiate and save the model.'))
