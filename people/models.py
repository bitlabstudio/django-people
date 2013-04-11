"""Models for the ``people`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from django_libs.models_mixins import SimpleTranslationMixin
from filer.fields.file import FilerFileField

from . import settings


GENDER_CHOICES = [
    ('male', _('male')),
    ('female', _('female')),
]

TITLE_CHOICES = [
    ('Dr', _('Dr')),
    ('Prof', _('Prof')),
    ('Prof Dr', _('Prof Dr')),
]


class LinkType(SimpleTranslationMixin, models.Model):
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

    class Meta:
        ordering = ['ordering', ]

    def __unicode__(self):
        return self.get_translation().name


class LinkTypeTranslation(models.Model):
    """
    Translateable fields of the ``LinkType`` model.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    # needed by simple-translation
    link_type = models.ForeignKey(LinkType)
    language = models.CharField(max_length=16)


class Role(SimpleTranslationMixin, models.Model):
    """
    People can have certain roles in an organisation.

    For translateable fields see ``RoleTranslation`` model.

    :name: The name of the role.

    """
    def __unicode__(self):
        return self.get_translation().name


class RoleTranslation(models.Model):
    """
    Translateable fields of the ``Role`` model.

    :name: The name of the role.

    """
    name = models.CharField(
        max_length=256,
        verbose_name=_('Role'),
    )

    role_description = models.TextField(
        max_length=4000,
        verbose_name=_('Role description'),
        blank=True,
    )

    # needed by simple-translation
    role = models.ForeignKey(Role)
    language = models.CharField(max_length=16)


class Person(SimpleTranslationMixin, models.Model):
    """
    A model that holds information about a person.

    For translateable fields see ``PersonTitle`` model.

    :gender: The gender of the person.
    :title: The title of the person.
    :chosen_name: For asian people, this is the chosen western name.
    :role: Role of the person within the organisation.
    :picture: A picture of the person.
    :phone: Phonenumber of the person.
    :email: Email address of the person.
    :ordering: Enter numbers if you want to order the list of persons on your
      site in a special way.

    """
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

    class Meta:
        ordering = ['ordering', ]

    def __unicode__(self):
        trans = self.get_translation()
        return '{0} {1}'.format(trans.first_name, trans.last_name)


class PersonTranslation(models.Model):
    """
    Translateable fields of the ``Person`` model.

    :first_name: The first name of the person. Must be translateable because
      for chinese people you might want to show chinese words vs. pinyin words
      depending on the users locale.
    :last_name: The last name of the person. Must be translateable (see
      first_name).
    :short_bio: A short description of the person.
    :bio: A longer description of the person, could appear after a
      ``read more`` link behind the ``short_bio``.

    """
    first_name = models.CharField(
        max_length=256,
        verbose_name=_('First name'),
    )

    last_name = models.CharField(
        max_length=256,
        verbose_name=_('Last anme'),
        blank=True,
    )

    short_bio = models.TextField(
        max_length=512,
        verbose_name=_('Short bio'),
        blank=True,
    )

    bio = models.TextField(
        max_length=4000,
        verbose_name=_('Biography'),
        blank=True,
    )

    # needed by simple-translation
    person = models.ForeignKey(Person)
    language = models.CharField(max_length=16)


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

    def __unicode__(self):
        return self.url
