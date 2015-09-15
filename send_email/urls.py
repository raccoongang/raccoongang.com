__author__ = 'vZ'

from django.conf.urls import patterns, url
from send_email import views


urlpatterns = patterns('', url(r'^$',views.send_email,name='send_email'),)
