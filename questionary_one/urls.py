__author__ = 'xahgmah'

from django.conf.urls import url
from django.views.defaults import page_not_found

from questionary_one.views import survey_view

urlpatterns = [
    url(r'^(?P<step>\d+)/$', survey_view, name='questionary'),
    url(r'^[[:ascii:]]*[^\x00-\x7F]+[[:ascii:]]*/$', page_not_found),
    url(r'^', survey_view),
]

