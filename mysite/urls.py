# -*- coding: utf-8 -*-
from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.views.defaults import page_not_found
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'send_email/',include('send_email.urls', namespace='send_email') ),
    url(r'^questionnaire/', include('questionary.urls')),
    # url(r'^question/', include('questionary_one.urls')),

    url(r'^', include('cms.urls')),
    # url(r'^[[:ascii:]]*[^\x00-\x7F]+[[:ascii:]]*/$', page_not_found),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA


urlpatterns += patterns('',
    url(r'^google5a92251e5fa234cc.html$', TemplateView.as_view(template_name="google5a92251e5fa234cc.html")),
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
)
