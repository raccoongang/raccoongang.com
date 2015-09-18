from django.db import models


# Create your models here.
class Block(models.Model):
    title = models.CharField(max_length=200)


    def __unicode__(self):
        return u'Title: %s' % self.title
