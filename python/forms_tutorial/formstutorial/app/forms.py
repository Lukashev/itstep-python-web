from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(required=True, strip=True)
    lastname = forms.CharField(required=True, strip=True)


class PrimeNumbersForm(forms.Form):
    start = forms.IntegerField(required=True)
    end = forms.IntegerField(required=True)


class ProfileInfoForm(UserForm):
    age = forms.IntegerField(required=True, min_value=0)
    gender = forms.ChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=(
            ('male', 'Male'),
            ('female', 'Female')
        )
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput
    )
