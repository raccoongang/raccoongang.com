from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
import eav
from adminsortable.models import SortableMixin


class Survey(models.Model):
    user = models.ForeignKey(User)
    is_draft = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s's survey" % self.user.username

eav.register(Survey)
pre_save.disconnect(eav.models.Entity.pre_save_handler, sender=Survey)


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
    formstep = models.ForeignKey('questionary.FormStep')
    image = models.ImageField(upload_to = 'uploads/')
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
