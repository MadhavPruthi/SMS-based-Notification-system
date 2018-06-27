from django import forms
from django.core.exceptions import ValidationError

from src.accounts.models import Student, Faculty


class SignUpStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data


class SignUpFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

    def clean(self):

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data
