from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .forms import MailForm
import json
from django.utils.translation import ugettext as _

from django.conf import settings

# Create your views here.

def send_email(request):
    if request.is_ajax():
        form = MailForm(request.GET)
        # if len(request.GET['message']) < 25:
        #     error_message = 'very small message!'
        errors = {}
        success = ''
        notification = ''
        if form.is_valid():
            form_data = form.cleaned_data
            #recipient_list = ['info@raccoongang.com']
            recipient_list = ['info@raccoongang.com']
            subject = form_data['name']
            message = 'From user email: %s \nMessage: \n %s' % (form_data['mail'],form_data['message'])

            #from_mail = form_data['mail']

            try:
                send_mail(subject, message, form_data['mail'], recipient_list, fail_silently=False)
                success = 'success'
                notification = _('Letter was sent, thank you')

                #response to email sending
                plaintext = get_template('email.txt')
                htmly     = get_template('main.html')

                d = Context({ 'username': form_data['name'] })

                subject, from_email, to = 'Thanks for your message to us', 'no-reply@raccoongang.com', form_data['mail']
                text_content = plaintext.render(d)
                html_content = htmly.render(d)

                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            except Exception as e:
                notification = _('Message has not been sent ' + e )
        else:
            for key in form.errors.keys():
                errors[key] = 'red'
        return HttpResponse(json.dumps({'errors': errors, 'notification': notification,
                                        'success': success}), content_type='application/json')
    return redirect('/')