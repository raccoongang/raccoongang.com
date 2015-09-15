from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from .forms import MailForm
import json

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
            recipient_list = ['info@raccoongang.com']
            subject = form_data['name']
            message = 'From user email: %s \nMessage: \n %s' % (form_data['mail'],form_data['message'])
            #from_mail = form_data['mail']
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)
                success = 'success'
                notification = _('The letter was sent, thank you for contacting us')
            except:
                notification = _('Message has not been sent')
        else:
            for key in form.errors.keys():
                errors[key] = 'red'
        return HttpResponse(json.dumps({'errors': errors, 'notification': notification,
                                        'success': success}), content_type='application/json')
    return redirect('/')