from django import forms
from .models import *


person = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    )


class SignInForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    person = forms.ChoiceField(choices=person)

    class Meta:
        model=User
        fields=('name', 'last_name', 'email','password', 'person')

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Confirm password field is not correct'
            )
