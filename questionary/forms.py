__author__ = 'xahgmah'
from copy import deepcopy
from django.forms import Textarea, SplitDateTimeWidget, ImageField
from eav.forms import BaseDynamicEntityForm
from questionary.models import Survey

class SurveyForm(BaseDynamicEntityForm):
    def __init__(self, data=None, *args, **kwargs):
        self.form_step = kwargs['form_step']
        del (kwargs['form_step'])
        super(BaseDynamicEntityForm, self).__init__(data, *args, **kwargs)
        config_cls = self.instance._eav_config_cls
        self.entity = getattr(self.instance, config_cls.eav_attr)
        self._build_dynamic_fields()

    class Meta:
        model = Survey
        fields = ['logo']

    def _build_dynamic_fields(self):
        # reset form fields
        self.fields = deepcopy(self.base_fields)
        if self.form_step.order != 1:
            del(self.fields['logo'])
        attributes = self.entity.get_all_attributes().filter(
            form_step=self.form_step).order_by('pk')
        for attribute in attributes:
            value = getattr(self.entity, attribute.slug)

            defaults = {
                'label': attribute.name.capitalize(),
                'required': attribute.required,
                'help_text': attribute.help_text,
                'validators': attribute.get_validators(),
            }

            datatype = attribute.datatype
            if datatype == attribute.TYPE_ENUM:
                enums = attribute.get_choices() \
                    .values_list('id', 'value')

                choices = [('', '-----')] + list(enums)

                defaults.update({'choices': choices})
                if value:
                    defaults.update({'initial': value.pk})

            # elif datatype == attribute.TYPE_DATE:
                # defaults.update({'widget': DateWidget})
            elif datatype == attribute.TYPE_TEXTAREA:
                defaults.update({'widget': Textarea})
            elif datatype == attribute.TYPE_OBJECT:
                continue

            MappedField = self.FIELD_CLASSES[datatype]
            self.fields[attribute.slug] = MappedField(**defaults)

            # fill initial data (if attribute was already defined)
            if value and not datatype == attribute.TYPE_ENUM:  # enum done above
                self.initial[attribute.slug] = value
        print self.fields

    def save(self, commit=True):
        """
        Saves this ``form``'s cleaned_data into model instance
        ``self.instance`` and related EAV attributes.

        Returns ``instance``.
        """

        if self.errors:
            raise ValueError(_(u"The %s could not be saved because the data"
                               u"didn't validate.") % \
                             self.instance._meta.object_name)

        # create entity instance, don't save yet
        instance = super(BaseDynamicEntityForm, self).save(commit=False)

        # assign attributes
        attributes = self.entity.get_all_attributes().filter(
            form_step=self.form_step).order_by('pk')
        for attribute in attributes:
            value = self.cleaned_data.get(attribute.slug)
            if attribute.datatype == attribute.TYPE_ENUM:
                if value:
                    value = attribute.enum_group.enums.get(pk=value)
                else:
                    value = None
            setattr(self.entity, attribute.slug, value)

        # save entity and its attributes
        if commit:
            instance.save()

        return instance
