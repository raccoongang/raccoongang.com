#-*- coding: utf-8 -*-
from django.db import models


class TestinonialsGallery(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return u'%s' % self.name


class Gallery(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return u'%s' % self.name


class Photo(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    button_title = models.CharField(max_length=128, null=True, blank=True)
    button_link = models.CharField(max_length=128, null=True, blank=True)
    file = models.ImageField(upload_to='images')
    gallery = models.ForeignKey(Gallery)

    def __str__(self):
        return u'%s' % self.title or self.file.name


class Testinonials(models.Model):
    text = models.CharField(max_length=1300, blank=True)
    client_name = models.CharField(max_length=150, blank=True)
    client_position = models.CharField(max_length=150, blank=True)
    link = models.CharField(max_length=128, blank=True)
    file = models.ImageField(upload_to='images')
    gallery = models.ForeignKey(TestinonialsGallery)

    def __str__(self):
        return u'%s' % self.client_name or self.file.name

