__author__ = 'xahgmah'
from copy import deepcopy
from django.forms import Textarea, SplitDateTimeWidget, ImageField, RadioSelect
from django.utils.html import conditional_escape, format_html, html_safe
from django.forms.utils import flatatt

from eav.forms import BaseDynamicEntityForm
from questionary.models import Survey


class MyRadioSelect(RadioSelect):


    def __init__(self, attrs=None, choices=()):
        super(MyRadioSelect, self).__init__(attrs)

    def render(self, name=None, value=None, attrs=None, choices=()):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        return format_html(
            '<label{}>{} {}</label>', label_for, self.tag(attrs), self.choice_label
        )
    #
    # def is_checked(self):
    #     return self.value == self.choice_value
    #
    def tag(self, attrs=None):
        attrs = attrs or self.attrs
        final_attrs = dict(attrs, type=self.input_type, name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return format_html('<input{} />', flatatt(final_attrs))


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
        if self.form_step.order != 4:
            del (self.fields['logo'])
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
            if datatype == attribute.TYPE_ENUM or \
                            datatype == attribute.TYPE_RADIO:
                enums = attribute.get_choices() \
                    .values_list('id', 'value')
                choices = list(enums)
                if datatype == attribute.TYPE_RADIO:
                    defaults.update({'widget': RadioSelect})
                else:
                    choices = [('', '-----')] + choices
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
            if value and datatype not in [attribute.TYPE_ENUM,
                                          attribute.TYPE_RADIO]:
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
