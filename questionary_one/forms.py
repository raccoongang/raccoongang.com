__author__ = 'xahgmah'
from copy import deepcopy
from django.forms import Textarea, CheckboxInput, EmailInput
from django.forms.widgets import RadioSelect
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.forms.utils import flatatt
from eav.forms import BaseDynamicEntityForm
from questionary.models import Survey


class CustomRadioRenderer(RadioSelect.renderer):
    def render(self):
        """Outputs radios"""
        output = '<div class="quiz_radio">'

        for w in self:
            html_str = '<label for="%s"><input id="%s" name="%s" ' \
                       'type="radio" value="%s" /><span><o></o></span><div>%s' \
                       '</div></label>' % (w.id_for_label,
                                           w.id_for_label,
                                           w.name,
                                           w.choice_value, w.choice_label)
            output += html_str
        output += '</div>'
        return output


class CustomCheckboxInput(CheckboxInput):
    def __init__(self, attrs=None, check_test=None, label=None):
        super(CustomCheckboxInput, self).__init__(attrs)
        self.label = label

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (
                        value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        return format_html(
            '<div class="quiz_checkbox"><label><input{}/><span><o></o></span><div>{}</div></label></div>',
            flatatt(final_attrs), self.label)


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
        fields = []

    def _build_dynamic_fields(self):
        # reset form fields
        self.fields = deepcopy(self.base_fields)
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
                    defaults.update(
                        {'widget': RadioSelect(renderer=CustomRadioRenderer)})
                else:
                    choices = [('', '-----')] + choices
                defaults.update({'choices': choices})
                if value:
                    defaults.update({'initial': value.pk})

                    # elif datatype == attribute.TYPE_DATE:
                    # defaults.update({'widget': DateWidget})
            elif datatype == attribute.TYPE_TEXTAREA:
                defaults.update({'widget': Textarea})
            elif datatype == attribute.TYPE_EMAIL:
                defaults.update({'widget': EmailInput})
            elif datatype == attribute.TYPE_BOOLEAN:
                defaults['label'] = ''
                defaults.update(
                    {'widget': CustomCheckboxInput(label=attribute.name)})
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
