#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Gallery, Photo


class GalleryAdmin(admin.ModelAdmin):
    fields = ['name']


class PhotoAdmin(admin.ModelAdmin):
    fields = ['title', 'file', 'gallery']

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
