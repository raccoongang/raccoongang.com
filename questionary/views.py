from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect
from questionary.models import FormStep, Survey, EdxProject
from questionary.forms import SurveyForm


def survey_view(request, projecthash, step=1):
    edp = EdxProject
    if edp.check_is_hash_expire(projecthash):
        messages.error(request, _(
            "Seems that this link is outdated. contact with our managers to get new one.."))
        return redirect('/')
    date, name, project_id = edp.decode_hash(projecthash)
    edx_project = get_object_or_404(
        EdxProject,
        pk=int(project_id)
    )
    form_step = get_object_or_404(
        FormStep,
        order=int(step)
    )
    max_order = FormStep.objects.all().aggregate(Max('order'))['order__max']
    params = {'edx_project': edx_project}
    try:
        survey = Survey.objects.filter(**params).latest('pk')
    except Survey.DoesNotExist:
        survey = Survey(**params)
        survey.save()
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
                    reverse('questionary', 'mysite.urls',
                            kwargs={
                                'projecthash': projecthash,
                                'step': go_to_step
                            }))
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
