from django.contrib import admin
from adminsortable.admin import SortableAdmin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
from eav.models import Attribute
from questionary.models import FormStep, Survey, FormGallery


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


admin.site.register(Survey, SurveyAdmin)
admin.site.register(FormStep, FormStepAdmin)
