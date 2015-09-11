from django.contrib import admin
from .models import Gallery, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'title', 'file','subtitle','button_title','button_link')


class BookInline(admin.TabularInline):
    model = Photo
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [BookInline]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
