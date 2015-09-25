from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from questionary.fields import OneToManyField
import eav
from adminsortable.models import SortableMixin


class Survey(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    is_draft = models.BooleanField(default=True)


eav.register(Survey)
pre_save.disconnect(eav.models.Entity.pre_save_handler, sender=Survey)


class FormStep(SortableMixin):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, editable=False,
                                        db_index=True, unique=True)
    attribute = OneToManyField('eav.Attribute')

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name

    def get_step_by_order(self):
        return self.order + 1


def pre_save_handler(sender, *args, **kwargs):
    '''
    Pre save handler attached to self.model.  Called before the
    model instance we are attached to is saved. This allows us to call
    :meth:`validate_attributes` before the entity is saved.
    '''
    instance = kwargs['instance']
    entity = getattr(kwargs['instance'], instance._eav_config_cls.eav_attr)
    entity.validate_attributes()
