"""django-cms plugins for the ``people`` app."""
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PersonPluginModel


class PersonPlugin(CMSPluginBase):
    model = PersonPluginModel
    name = _("Person Plugin")
    render_template = "people/person_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'plugin': instance,
            'person': instance.person,
            'display_type': instance.display_type,
        })
        return context


plugin_pool.register_plugin(PersonPlugin)
