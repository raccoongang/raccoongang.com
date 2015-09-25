__author__ = 'xahgmah'

from django.conf.urls import url
from questionary.views import survey_view,complete_view


urlpatterns = [
    url(r'^complete/', complete_view, name='complete'),
    url(r'^(?P<step>\d+)/$', survey_view, name='questionary'),
    url(r'^', survey_view),
]