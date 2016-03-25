# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models


class ContactUsEmail(models.Model):
    text = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.date.strftime("%d-%m-%Y, %H:%M") + ' - ' + self.email
