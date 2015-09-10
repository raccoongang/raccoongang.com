from django.db import models
from cms.models import CMSPlugin
from core.models import Block


class CallToActionPlugin(CMSPlugin):
    block_to_show = models.ForeignKey(Block)

    def __unicode__(self):
        return self.block_to_show.title

# Create your models here.
