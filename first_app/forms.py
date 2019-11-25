from django import forms
from django.core import validators

# def check_for_Z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NEEDS TO START WITH Z')
#* in name charfiled put 'validators=[check_for_Z]' to make check for z work

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

   