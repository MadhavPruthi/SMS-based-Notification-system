from django import forms
from django.core.exceptions import ValidationError
from .models import Student, Faculty


class SignUpStudentForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        exclude = ('User',)
        model = Student

    def clean(self):

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data


class SignUpFacultyForm(forms.ModelForm):

    class Meta:
        exclude = ('User',)
        model = Faculty

    def clean(self):

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data
