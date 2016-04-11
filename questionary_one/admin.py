from django.contrib import admin
from adminsortable.admin import SortableAdmin
from django.utils.safestring import mark_safe
from eav_one.forms import BaseDynamicEntityForm
from eav_one.admin import BaseEntityAdmin
from eav_one.models import Attribute
from django import forms
from questionary_one.models import FormStep, Survey, FormGallery, EdxProject


def generate_fieldsets():
    fieldsets = (None, {'fields': ('edx_project', 'is_draft', 'logo')}),

    for form_step in FormStep.objects.all():
        fieldset_fields = ()
        attributes = Attribute.on_site.all().filter(
            form_step=form_step).order_by('pk')
        for attribute in attributes:
            # #     for attribute in self.entity.get_all_attributes():
            fieldset_fields += (str(attribute.slug),)
        fieldsets += (form_step.name, {'fields': fieldset_fields}),
    return fieldsets


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


class SurveyAdmin(admin.ModelAdmin):
    form = SurveyAdminForm

    def render_change_form(self, request, context, add=False, change=False,
                           form_url='', obj=None):
        form = context['adminform'].form
        fieldsets = generate_fieldsets()
        adminform = admin.helpers.AdminForm(form, fieldsets,
                                            self.prepopulated_fields)
        media = mark_safe(self.media + adminform.media)

        context.update(adminform=adminform, media=media)

        super_meth = super(SurveyAdmin, self).render_change_form
        return super_meth(request, context, add, change, form_url, obj)


class EdxProjectAdminForm(forms.ModelForm):
    widget = forms.Textarea
    link = forms.CharField(required=False, widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super(EdxProjectAdminForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         if instance.expire_date:
    #             self.initial['link'] = instance.generate_url()
    #     self.fields['link'].widget.attrs['readonly'] = True

    class Meta:
        model = EdxProject
        fields = ['name']


class EdxProjectAdmin(admin.ModelAdmin):
    form = EdxProjectAdminForm


admin.site.register(EdxProject, EdxProjectAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(FormStep, FormStepAdmin)
