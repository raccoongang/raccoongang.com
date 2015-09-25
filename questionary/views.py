from django.core.urlresolvers import reverse
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render
from questionary.models import FormStep, Survey
from questionary.forms import SurveyForm


@login_required
def survey_view(request, step=1):
    form_step = get_object_or_404(
        FormStep,
        order=int(step)
    )
    max_order = FormStep.objects.all().aggregate(Max('order'))['order__max']
    survey, created = Survey.objects.get_or_create(user=request.user,
                                                   is_draft=True)
    form = SurveyForm(instance=survey, form_step=form_step)

    if request.method == 'POST':
        params = request.POST.copy()
        go_to_step = int(params['form_step'])
        del (params['form_step'])
        form = SurveyForm(request.POST, instance=survey, form_step=form_step)
        if form.is_valid():
            form.save()
            if go_to_step == -1:
                form.instance.is_draft = False
                form.instance.save()
                return HttpResponseRedirect(
                    reverse('questionary:complete'))
            else:
                return HttpResponseRedirect(
                    reverse('questionary:questionary',
                            kwargs={'step': go_to_step}))

    return render(request, 'form_step.html',
                  {
                      'form_step': form_step,
                      'form': form,
                      'max_order': max_order
                  })


def complete_view(request):
    message = _("Data has successfully saved.")
    return render(request, 'complete.html',
                  {
                      'message': message,
                  })
