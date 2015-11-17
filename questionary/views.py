from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect
from questionary.models import FormStep, Survey, EdxProject
from questionary.forms import SurveyForm


def survey_view(request, step=1):
    if 'project_pk' in request.session.keys():
        edx_project = EdxProject.objects.get(pk=request.session['project_pk'])
    else:
        edx_project = EdxProject(name='name')
        edx_project.save()
        request.session['project_pk'] = edx_project.pk
    all_steps = FormStep.objects.all().order_by('order').values_list('name', flat=True)
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
        form = SurveyForm(params,
                          request.FILES,
                          instance=survey,
                          form_step=form_step)
        if form.is_valid():
            try:
                if form.cleaned_data['main_name']:
                    edx_project.name=form.cleaned_data['main_name']
                    edx_project.save()
                    print edx_project
            except Exception as e:
                print e
            form.save()
            if go_to_step == -1:
                form.instance.is_draft = False
                form.instance.save()
                messages.success(request,
                                 _("Data has been successfully saved."))
                return redirect('/')
            else:
                return HttpResponseRedirect(
                    reverse('questionary', 'mysite.urls',
                            kwargs={
                                # 'projecthash': projecthash,
                                'step': go_to_step
                            }))
    else:
        form = SurveyForm(instance=survey, form_step=form_step)

    return render(request, 'form_step.html',
                  {
                      'session':request.session['project_pk'],
                      'all_steps':all_steps,
                      'form_step': form_step,
                      'form': form,
                      'max_order': max_order,
                      'max_order_range': range(1, max_order+1),
                      'step_width': 100 / max_order,
                  })
