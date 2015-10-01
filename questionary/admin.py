from django.contrib import admin
from adminsortable.admin import SortableAdmin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from eav.models import Attribute
from django import forms
from questionary.models import FormStep, Survey, FormGallery, EdxProject


class AttributeInline(admin.StackedInline):
    model = Attribute
    exclude = ('site', 'type')


class GalleryInline(admin.StackedInline):
    model = FormGallery


class FormStepAdmin(SortableAdmin):
    inlines = [
        AttributeInline,
        GalleryInline,
    ]

    class Media:
        js = (
            'admin/js/prepopulate.js', 'admin/js/urlify.js', 'js/slugify.js',)


class SurveyAdminForm(BaseDynamicEntityForm):
    model = Survey


class SurveyAdmin(BaseEntityAdmin):
    form = SurveyAdminForm


class EdxProjectAdminForm(forms.ModelForm):
    widget = forms.Textarea
    link = forms.CharField(required=False,widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(EdxProjectAdminForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            if instance.expire_date:
                self.initial['link'] = instance.generate_url()
        self.fields['link'].widget.attrs['readonly'] = True

    class Meta:
        model = EdxProject
        fields = ['name', 'expire_date', 'link']


class EdxProjectAdmin(admin.ModelAdmin):
    form = EdxProjectAdminForm


admin.site.register(EdxProject, EdxProjectAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(FormStep, FormStepAdmin)
