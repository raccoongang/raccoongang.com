from django.db import models


# Create your models here.
class Block(models.Model):
    title = models.CharField(max_length=200)
    button_title = models.CharField(max_length=100)
    button_link = models.CharField(max_length=100)

    def __str__(self):
        return u'Title:%s Button:%s Link:%s' % (self.title, self.button_title, self.button_link)
