__author__ = 'vZ'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from call_to_action_plugin.models import CallToActionPlugin
from django.utils.translation import ugettext as _


class CMSCallToActionPlugin(CMSPluginBase):  # plugin for call to action block
    model = CallToActionPlugin
    name = _("Call to action block")
    render_template = "djangocms_call_to_action/call_to_action_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(CMSCallToActionPlugin)  # register the plugin
