__author__ = 'vZ'
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from django.contrib import admin

from top_gallery_plugin.models import TopGalleryPlugin
from clients_plugin.models import ClientsPlugin
from testinonials.models import TestinonialsPlugin


class CMSTopGalleryPlugin(CMSPluginBase):  #plugin for gallery block
    model = TopGalleryPlugin
    name = _("Top gallery")
    admin_preview = True
    #inlines = (BookInline, )
    change_form_template = "djangocms_top_gallery/top_gallery_plugin_form.html"
    render_template = "djangocms_top_gallery/top_gallery_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class CMSClientsPlugin(CMSPluginBase):  #plugin for clients block
    model = ClientsPlugin
    name = _("Clients")
    admin_preview = True
    change_form_template = "djangocms_clients/clients_plugin_form.html"
    render_template = "djangocms_clients/clients_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class CMSTestinonialsPlugin(CMSPluginBase):  #plugin for clients block
    model = TestinonialsPlugin
    name = _("Testinonials")
    admin_preview = True
    # change_form_template = "djangocms_clients/clients_plugin_form.html"
    render_template = "djangocms_testinonials/testinonials_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSTopGalleryPlugin)  # register the plugin
plugin_pool.register_plugin(CMSClientsPlugin)  # register the plugin
plugin_pool.register_plugin(CMSTestinonialsPlugin)  # register the plugin