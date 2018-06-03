from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class Student_signup_form(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        fields = ('SID', 'name','DOB','Branch','Year_Of_Study','Semester','Contact' , 'email', 'password1', 'password2', )
        model = Student

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['Branch'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
            self.fields['Year_Of_Study'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
            self.fields['Semester'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
            self.fields['Contact_Number'].widget.attrs['class'] = 'form-control'
