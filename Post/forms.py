from django import forms
from .models import * 


class ContactForm(forms.Form):
    from_email  = forms.EmailField()
    subject  = forms.CharField(max_length=25)
    message  = forms.CharField(required=True,widget=forms.Textarea)
