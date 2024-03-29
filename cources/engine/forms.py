from django import forms
from .models import *


person = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    )


class SignInForm(forms.Form):
    email = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    person = forms.ChoiceField(choices=person)

    class Meta:
        model=Student
        fields=('name', 'last_name', 'email','password', 'person')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Confirm password field is not correct'
            )
