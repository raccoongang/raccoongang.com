#-*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import get_thumbnail


class Gallery(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return u'%s' % self.name


class Photo(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    file = models.ImageField(upload_to='images')
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return u'%s' % self.title or self.file.name

    def slide_thumbnail(self):
        print(self.file.url)
        return '<img src="%s" width=15%/>' % (self.file.url)
    slide_thumbnail.allow_tags = True


