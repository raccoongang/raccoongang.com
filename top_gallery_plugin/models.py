from django.db import models
from cms.models import CMSPlugin
from top_gallery.models import Gallery


class TopGalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(Gallery)


    def __unicode__(self):
        return self.gallery.name

