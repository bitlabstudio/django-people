"""Admin classes for the ``people`` app."""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from hvad.admin import TranslatableAdmin

from . import models


class NationalityAdmin(TranslatableAdmin):
    """Admin for the ``Nationality`` model."""
    list_display = ['get_name', 'all_translations']
    list_select_related = []

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


class LinkAdmin(admin.ModelAdmin):
    """Admin for the ``Link`` model."""
    list_display = ['person', 'link_type', 'url', ]


class LinkInline(admin.TabularInline):
    """Inline admin for ``Link`` objects."""
    model = models.Link


class LinkTypeAdmin(TranslatableAdmin):
    """Admin for the ``LinkType`` model."""
    list_display = ['get_name', 'ordering', 'all_translations', ]
    list_select_related = []

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


class PersonAdmin(TranslatableAdmin):
    """Admin for the ``Person`` model."""
    inlines = [LinkInline, ]
    list_display = [
        'roman_first_name', 'roman_last_name', 'non_roman_first_name_link',
        'non_roman_last_name', 'chosen_name', 'gender', 'title', 'role',
        'phone', 'email', 'ordering', 'all_translations', ]
    list_select_related = []

    def non_roman_first_name_link(self, obj):
        return u'<a href="{0}/">{1}</a>'.format(
            obj.pk, obj.non_roman_first_name)
    non_roman_first_name_link.allow_tags = True
    non_roman_first_name_link.short_description = "Non roman first name"


class RoleAdmin(TranslatableAdmin):
    """Admin for the ``Role`` model."""
    list_display = ['get_name', 'all_translations', ]
    list_select_related = []

    def get_name(self, obj):
        return obj.name
    get_name.short_description = _('Name')


admin.site.register(models.Nationality, NationalityAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.LinkType, LinkTypeAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Role, RoleAdmin)
