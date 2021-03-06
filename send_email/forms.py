from django import forms


class MailForm(forms.Form):
    name = forms.CharField(max_length=50)
    mail = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=5000)