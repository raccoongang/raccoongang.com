from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from eav.models import Value
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


from django.shortcuts import get_object_or_404, render, redirect
from questionary.models import FormStep, Survey, EdxProject
from questionary.forms import SurveyForm


def send_survey_email(info, organisation):
    recipient_list = ['info@raccoongang.com']
    subject = 'Survey from %s' % organisation

    #from_mail = form_data['mail']

    #response to email sending
    htmly = get_template('survey_email.html')

    d = Context({'dict':info})

    html_content = htmly.render(d)
    from_email = 'survey@raccoongang.com'

    msg = EmailMultiAlternatives(subject=subject, from_email=from_email,
                                     to=recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_customer_email(customer_email, customer_name):
    d = Context({ 'username': customer_name })

    plaintext = get_template('email.txt')
    htmly     = get_template('main.html')

    subject, from_email, to = 'Thanks for your message to us', 'no-reply@raccoongang.com', customer_email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def survey_view(request, step=1):
    if 'project_pk' in request.session.keys():
        edx_project = EdxProject.objects.get(pk=request.session['project_pk'])
        print request.session['project_pk']
    else:
        edx_project = EdxProject(name='name')
        edx_project.save()
        request.session['project_pk'] = edx_project.pk
        request.session.set_expiry(172000)
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
                if form.cleaned_data['organization']:
                    edx_project.name=form.cleaned_data['organization']
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

                survey = Survey.objects.get(edx_project=edx_project)
                for_email = []
                organisation, first_name = '', ''
                print survey.eav.get_all_attributes()
                for attribute in survey.eav.get_all_attributes():
                    for_email.append({attribute.name:getattr(survey.eav, attribute.slug)})
                    if attribute.datatype == 'email':
                        customer_email = getattr(survey.eav, attribute.slug)
                    if attribute.name == 'First Name':
                        first_name = getattr(survey.eav, attribute.slug)
                    if attribute.name == 'Organisation':
                        organisation = getattr(survey.eav, attribute.slug)
                send_survey_email(for_email, organisation)
                send_customer_email(customer_email, first_name)

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
                      'all_steps':all_steps,
                      'form_step': form_step,
                      'form': form,
                      'max_order': max_order,
                      'max_order_range': range(1, max_order+1),
                      'step_width': 100 / max_order,
                  })
