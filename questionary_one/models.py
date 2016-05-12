# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
import eav_one
from adminsortable.models import SortableMixin
from django.contrib.sites.models import Site


class EdxProject(models.Model):
    name = models.CharField(max_length=48)
    expire_date = models.DateField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.name

    # def generate_url(self):
    #     current_site = Site.objects.get_current()
    #
    #     url = reverse('questionary', 'mysite.urls', kwargs={
    #         'projecthash': self.generate_hash(),
    #         'step': 1
    #     })
    #     return 'http://' + current_site.domain + url

    # def generate_hash(self):
    #     data = ",".join(str(i) for i in (self.expire_date, self.name, self.pk))
    #     return base64.urlsafe_b64encode(data)
    #
    # @staticmethod
    # def decode_hash(hash):
    #     return base64.urlsafe_b64decode(str(hash)).split(',')
    #
    # @staticmethod
    # def check_is_hash_expire(hash):
    #     try:
    #         date, name, id = EdxProject.decode_hash(hash)
    #     except:
    #         return True
    #     date_format = "%Y-%m-%d"
    #     return datetime.strptime(date,
    #                              date_format).date() < datetime.now().date()
    #
    # link = None


class Survey(models.Model):
    edx_project = models.ForeignKey(EdxProject)
    is_draft = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='images', blank=True)

    def __unicode__(self):
        return u"Survey for %s" % self.edx_project.name


eav_one.register(Survey)
pre_save.disconnect(eav_one.models.Entity.pre_save_handler, sender=Survey)


class FormStep(SortableMixin):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name


class FormGallery(SortableMixin):
    name = models.CharField(max_length=64)
    data_attribute = models.CharField(max_length=64)
    formstep = models.ForeignKey('questionary_one.FormStep')
    image = models.ImageField(upload_to='uploads/')
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name


def pre_save_handler(sender, *args, **kwargs):
    '''
    Pre save handler attached to self.model.  Called before the
    model instance we are attached to is saved. This allows us to call
    :meth:`validate_attributes` before the entity is saved.
    '''
    instance = kwargs['instance']
    entity = getattr(kwargs['instance'], instance._eav_config_cls.eav_attr)
    entity.validate_attributes()
