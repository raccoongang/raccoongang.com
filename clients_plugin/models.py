from django.db import models
from cms.models import CMSPlugin
from top_gallery.models import Gallery


class ClientsPlugin(CMSPlugin):
    clients = models.ForeignKey(Gallery)

    def __str__(self):
        return self.clients.name


