from django.contrib import admin
from .models import Gallery, Photo, Testinonials, TestinonialsGallery


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'title', 'file','subtitle','button_title','button_link')


class BookInline(admin.TabularInline):
    model = Photo
    extra = 0

class TestinonialsAdmin(admin.ModelAdmin):
    list_display = ('text', 'client_name', 'file','link')


class GalleryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [BookInline]

class ClientInline(admin.TabularInline):
    model = Testinonials
    extra = 0

class TestinonialsGalleryAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [ClientInline]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Testinonials, TestinonialsAdmin)
admin.site.register(TestinonialsGallery, TestinonialsGalleryAdmin)