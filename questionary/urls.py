__author__ = 'xahgmah'

from django.conf.urls import url
from questionary.views import survey_view

urlpatterns = [
    url(r'^(?P<step>\d+)/$', survey_view, name='questionary'),
    url(r'^', survey_view),
]

