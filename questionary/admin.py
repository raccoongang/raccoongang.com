from django.contrib import admin
from adminsortable.admin import SortableAdmin
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

from questionary.models import FormStep, Survey

class AttributeInline(admin.StackedInline):
    model = FormStep.attribute.through


class FormStepAdmin(SortableAdmin):
    inlines = [
        AttributeInline,
    ]
    exclude = ('attribute',)



class SurveyAdminForm(BaseDynamicEntityForm):
    model = Survey


class SurveyAdmin(BaseEntityAdmin):
    form = SurveyAdminForm


admin.site.register(Survey, SurveyAdmin)
admin.site.register(FormStep, FormStepAdmin)
