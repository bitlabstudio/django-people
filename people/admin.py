"""Admin classes for the ``people`` app."""
from django.contrib import admin
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _

from simple_translation.admin import TranslationAdmin
from simple_translation.utils import get_preferred_translation_from_lang

from . import models


class NationalityAdmin(TranslationAdmin):
    """Admin for the ``Nationality`` model."""
    list_display = ['name', 'languages']

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


class LinkAdmin(admin.ModelAdmin):
    """Admin for the ``Link`` model."""
    list_display = ['person', 'link_type', 'url', ]


class LinkInline(admin.TabularInline):
    """Inline admin for ``Link`` objects."""
    model = models.Link


class LinkTypeAdmin(TranslationAdmin):
    """Admin for the ``LinkType`` model."""
    list_display = ['name', 'ordering', 'languages', ]

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


class PersonAdmin(TranslationAdmin):
    """Admin for the ``Person`` model."""
    inlines = [LinkInline, ]
    list_display = [
        'roman_first_name', 'roman_last_name', 'non_roman_first_name_link',
        'non_roman_last_name', 'chosen_name', 'gender', 'title', 'role',
        'phone', 'email', 'ordering', 'languages', ]

    def non_roman_first_name_link(self, obj):
        return u'<a href="{}/">{}</a>'.format(
            obj.pk, unicode(obj.non_roman_first_name))
    non_roman_first_name_link.allow_tags = True
    non_roman_first_name_link.short_description = "Non roman first name"


class RoleAdmin(TranslationAdmin):
    """Admin for the ``Role`` model."""
    list_display = ['name', 'languages', ]

    def name(self, obj):
        lang = get_language()
        return get_preferred_translation_from_lang(obj, lang).name
    name.short_description = _('Name')


admin.site.register(models.Nationality, NationalityAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkType, LinkTypeAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Role, RoleAdmin)
