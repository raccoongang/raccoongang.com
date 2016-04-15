from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db.models import Max
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect

from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


from django.shortcuts import get_object_or_404, render
from questionary_one.models import FormStep, Survey, EdxProject
from questionary_one.forms import SurveyForm


def send_survey_email(info):
    recipient_list = ['info@raccoongang.com']
    # recipient_list = ['i.batozskiy@gmail.com']
    subject = 'Survey from %s' % info['name']

    #from_mail = form_data['mail']

    #response to email sending
    htmly = get_template('survey_email_one.html')

    d = Context({'dict':info})

    html_content = htmly.render(d)
    from_email = 'survey@raccoongang.com'

    msg = EmailMultiAlternatives(subject=subject, from_email=from_email,
                                     to=recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_customer_email(customer_email, customer_name, info):
    d = Context({'username': customer_name, 'dict': info})

    plaintext = get_template('email.txt')
    htmly = get_template('survey_main.html')

    subject = 'Request for an Open edX services from %s %s' % (customer_name.capitalize(),
                                                            info['surname'].capitalize())
    from_email = 'info@raccoongang.com'

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [customer_email], cc=['info@raccoongang.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def survey_view(request, step=1):
    if 'survey_pk' in request.session.keys():
        edx_project = EdxProject.objects.get(pk=request.session['survey_pk'])
    else:
        edx_project = EdxProject(name='name')
        edx_project.save()
        request.session['survey_pk'] = edx_project.pk
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
                if form.cleaned_data['name']:
                    edx_project.name=form.cleaned_data['name']
                    edx_project.save()
            except Exception as e:
                print e
            form.save()
            if go_to_step == -1:
                form.instance.is_draft = False
                form.instance.save()
                messages.add_message(request, messages.INFO,
                                 _("Thank you for choosing our company.| We will contact you within a business day."))
                survey = Survey.objects.get(edx_project=edx_project)
                for_email = []
                for attribute in survey.eav.get_all_attributes():
                    for_email.append((attribute.slug, getattr(survey.eav, attribute.slug)))
                    if attribute.datatype == 'e-mail':
                        customer_email = getattr(survey.eav, attribute.slug)
                try:
                    send_survey_email(dict(for_email))
                    send_customer_email(customer_email, dict(for_email)['name'], dict(for_email))
                except Exception as e:
                    print e
                return HttpResponseRedirect(reverse('cms.views.details', kwargs={'slug': ''}))
            else:
                return HttpResponseRedirect(
                    reverse('questionary_one', 'mysite.urls',
                            kwargs={
                                'step': go_to_step
                            }))
    else:
        form = SurveyForm(instance=survey, form_step=form_step)
    return render(request, 'form_step_one.html',
                  {
                      'all_steps':all_steps,
                      'form_step': form_step,
                      'form': form,
                      'max_order': max_order,
                      'max_order_range': range(1, max_order+1),
                      'step_width': 100 / max_order,
                  })
