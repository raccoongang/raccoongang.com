#-*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import get_thumbnail


class Gallery(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return u'%s' % self.name


class Photo(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    file = models.ImageField(upload_to='images')
    gallery = models.ForeignKey(Gallery)

    def __str__(self):
        return u'%s' % self.title or self.file.name

    def slide_thumbnail(self):
        print(self.file.url)
        return '<img src="'+self.file.url+'" width=15%/>'
    slide_thumbnail.allow_tags = True


