from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(required=True, strip=True)
    lastname = forms.CharField(required=True, strip=True)