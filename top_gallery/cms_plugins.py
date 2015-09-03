__author__ = 'vZ'
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from top_gallery_plugin.models import TopGalleryPlugin
from django.utils.translation import ugettext as _


class CMSTopGalleryPlugin(CMSPluginBase):
    model = TopGalleryPlugin  # model where plugin data are saved
    #module =
    name = _("Top gallery")  # name of the plugin in the interface
    render_template = "djangocms_top_gallery/top_gallery_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSTopGalleryPlugin)  # register the plugin