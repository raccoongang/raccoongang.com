from django.contrib import admin
from adminsortable.admin import SortableAdmin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from questionary.models import FormStep, Survey, FormGallery


class AttributeInline(admin.StackedInline):
    model = FormStep.attribute.through


class GalleryInline(admin.StackedInline):
    model = FormGallery


class FormStepAdmin(SortableAdmin):
    inlines = [
        AttributeInline,
        GalleryInline,
    ]
    exclude = ('attribute',)


class SurveyAdminForm(BaseDynamicEntityForm):
    model = Survey


class SurveyAdmin(BaseEntityAdmin):
    form = SurveyAdminForm


admin.site.register(Survey, SurveyAdmin)
admin.site.register(FormStep, FormStepAdmin)
