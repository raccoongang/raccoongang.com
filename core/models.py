from django.db import models


# Create your models here.
class Block(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    button_title = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Title: %s' % (self.title)
