from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect
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
    if request.method == 'POST':
        params = request.POST.copy()
        go_to_step = int(params['form_step'])
        del (params['form_step'])
        form = SurveyForm(params, instance=survey, form_step=form_step)
        if form.is_valid():
            form.save()
            if go_to_step == -1:
                form.instance.is_draft = False
                form.instance.save()
                messages.success(request, _("Data has successfully saved."))
                return redirect('/')
            else:
                return HttpResponseRedirect(
                    reverse('questionary:questionary',
                            kwargs={'step': go_to_step}))
    else:
        form = SurveyForm(instance=survey, form_step=form_step)

    return render(request, 'form_step.html',
                  {
                      'form_step': form_step,
                      'form': form,
                      'max_order': max_order,
                      'progress': round(
                          100 / max_order * (form_step.order - 1)
                      )
                  })
