from django import forms
from django.core import validators

# def check_for_Z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NEEDS TO START WITH Z')
#* in name charfiled put 'validators=[check_for_Z]' to make check for z work

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
       all_clean_data = super().clean()
       email = all_clean_data['email']
       vmail = all_clean_data['verify_email']

       if email != vmail:
           raise forms.ValidationError('MAKE SURE EMAILS MATCH')