__author__ = 'xahgmah'

from django.conf.urls import url
from questionary.views import survey_view

urlpatterns = [
    url(r'^(?P<projecthash>[0-9A-Za-z_+=]+)/(?P<step>\d+)/$', survey_view, name='questionary'),
    # url(r'^', survey_view),
]
