"""Models for the ``people`` app."""
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.file import FilerFileField
from hvad.models import TranslatedFields, TranslatableModel
from localized_names.templatetags.localized_names_tags import get_name

from . import settings


# Hack to have these strings translated
mr = _('Mr')
mrs = _('Ms')


GENDER_CHOICES = [
    ('male', _('male')),
    ('female', _('female')),
]

TITLE_CHOICES = [
    ('Dr', _('Dr')),
    ('Prof', _('Prof')),
    ('Prof Dr', _('Prof Dr')),
]


@python_2_unicode_compatible
class LinkType(TranslatableModel):
    """
    A link type could be ``Facebook`` or ``Twitter`` or ``Website``.

    This is masterdata that should be created by the admins when the site is
    deployed for the first time.

    For translateable fields see ``LinkTypeTranslation`` model.

    :ordering: Enter numbers here if you want links to be displayed in a
      special order.

    """
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
        help_text=_(
            'Use this field to define a simple identifier that can be used'
            ' to style the different link types (i.e. assign social media'
            ' icons to them)'),
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'),
        null=True, blank=True,
    )

    translations = TranslatedFields(
        name=models.CharField(
            max_length=256,
            verbose_name=_('Name'),
        )
    )

    class Meta:
        ordering = ['ordering', ]

    def __str__(self):
        return self.safe_translation_getter('name', self.slug)


@python_2_unicode_compatible
class Nationality(TranslatableModel):
    """
    The nationality of a Person.

    For translateable fields see the ``NationalityTranslation`` model.

    """
    translations = TranslatedFields(
        name=models.CharField(
            max_length=128,
            verbose_name=_('Name'),
        )
    )

    def __str__(self):
        return self.safe_translation_getter(
            'name', 'Nationality No. {0}'.format(self.id))

    class Meta:
        verbose_name_plural = _('Nationalities')


@python_2_unicode_compatible
class Role(TranslatableModel):
    """
    People can have certain roles in an organisation.

    For translateable fields see ``RoleTranslation`` model.

    :name: The name of the role.

    """
    translations = TranslatedFields(
        name=models.CharField(
            max_length=256,
            verbose_name=_('Role'),
        ),
        role_description=models.TextField(
            max_length=4000,
            verbose_name=_('Role description'),
            blank=True,
        ),
    )

    def __str__(self):
        return self.safe_translation_getter(
            'name', 'Role No. {0}'.format(self.id))


@python_2_unicode_compatible
class Person(TranslatableModel):
    """
    A model that holds information about a person.

    For translateable fields see ``PersonTitle`` model.

    :roman_first_name: The first name in roman letters.
    :roman_last_name: The last name in roman letters.
    :non_roman_first_name: The first name in non roman letters.
    :non_roman_last_name: The last name in non roman letters.
    :gender: The gender of the person.
    :title: The title of the person.
    :chosen_name: For asian people, this is the chosen western name.
    :role: Role of the person within the organisation.
    :picture: A picture of the person.
    :phone: Phonenumber of the person.
    :email: Email address of the person.
    :ordering: Enter numbers if you want to order the list of persons on your
      site in a special way.
    :nationality: The nationality of a person.

    """
    roman_first_name = models.CharField(
        max_length=256,
        verbose_name=_('Roman first name'),
        blank=True
    )

    roman_last_name = models.CharField(
        max_length=256,
        verbose_name=_('Roman last name'),
        blank=True,
    )

    non_roman_first_name = models.CharField(
        max_length=256,
        verbose_name=_('Non roman first name'),
        blank=True
    )

    non_roman_last_name = models.CharField(
        max_length=256,
        verbose_name=_('Non roman last name'),
        blank=True,
    )

    gender = models.CharField(
        max_length=16,
        choices=GENDER_CHOICES,
        verbose_name=_('Gender'),
        blank=True,
    )

    title = models.CharField(
        max_length=16,
        choices=TITLE_CHOICES,
        verbose_name=_('Title'),
        blank=True,
    )

    chosen_name = models.CharField(
        max_length=256,
        verbose_name=_('Chosen name'),
        blank=True,
    )

    role = models.ForeignKey(
        Role,
        verbose_name=_('Role'),
        null=True, blank=True,
    )

    picture = FilerFileField(
        verbose_name=_('Picture'),
        null=True, blank=True,
    )

    phone = models.CharField(
        max_length=32,
        verbose_name=_('Phone'),
        blank=True,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        verbose_name=_('Ordering'),
        null=True, blank=True,
    )

    nationality = models.ForeignKey(
        Nationality,
        verbose_name=_('Nationality'),
        blank=True, null=True,
    )

    translations = TranslatedFields(
        short_bio=models.TextField(
            max_length=512,
            verbose_name=_('Short bio'),
            blank=True,
        ),
        bio=models.TextField(
            max_length=4000,
            verbose_name=_('Biography'),
            blank=True,
        ),
    )

    class Meta:
        ordering = ['ordering', ]
        verbose_name_plural = _('People')

    def __str__(self):
        return get_name(self)

    def get_gender(self):
        """Returns either 'Mr.' or 'Ms.' depending on the gender."""
        if self.gender == 'male':
            return 'Mr'
        elif self.gender == 'female':
            return 'Ms'
        return ''

    def get_title(self):
        """Returns the title of the person."""
        return self.title

    def get_romanized_first_name(self):
        """Returns the first name in roman letters."""
        return self.roman_first_name

    def get_romanized_last_name(self):
        """Returns the first name in roman letters."""
        return self.roman_last_name

    def get_non_romanized_first_name(self):
        """Returns the non roman version of the first name."""
        return self.non_roman_first_name

    def get_non_romanized_last_name(self):
        """Returns the non roman version of the first name."""
        return self.non_roman_last_name

    def get_nickname(self):
        """Returns the nickname of a person in roman letters."""
        return self.chosen_name


class PersonPluginModel(CMSPlugin):
    """Model for the ``PersonPlugin`` cms plugin."""
    display_type = models.CharField(
        max_length=256,
        choices=settings.DISPLAY_TYPE_CHOICES,
        verbose_name=_('Display type'),
    )

    person = models.ForeignKey(
        Person,
        verbose_name=_('Person'),
    )

    def copy_relations(self, oldinstance):
        self.person = oldinstance.person


@python_2_unicode_compatible
class Link(models.Model):
    """
    A person can have many links.

    """
    person = models.ForeignKey(
        Person,
        verbose_name=_('Person'),
    )

    link_type = models.ForeignKey(
        LinkType,
        verbose_name=_('Link type'),
    )

    url = models.URLField(
        verbose_name=_('URL'),
    )

    def __str__(self):
        return self.url
