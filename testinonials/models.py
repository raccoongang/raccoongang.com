from django.db import models
from cms.models import CMSPlugin
from top_gallery.models import TestinonialsGallery


class TestinonialsPlugin(CMSPlugin):
    gallery = models.ForeignKey(TestinonialsGallery)

    def __unicode__(self):
        return self.gallery.name
