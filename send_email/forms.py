from django import forms


class MailForm(forms.Form):
    name = forms.CharField(max_length=30)
    mail = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=1000)