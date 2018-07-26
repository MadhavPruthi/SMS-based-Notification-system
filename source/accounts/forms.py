from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Student, Faculty, FacultyCourse, StudentCourse


class SignUpStudentForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        exclude = ('User',)
        model = Student

    def clean(self):

        # print(self.cleaned_data)
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        StudentID = self.cleaned_data['StudentID']

        if StudentID:

            try:
                Student.objects.get(StudentID=StudentID)
                raise ValidationError("Student ID already exists!", code="ID error")

            except ObjectDoesNotExist:
                pass

            if 16101000 < int(StudentID) < 16108999:
                pass
            else:
                raise ValidationError("Student ID is no valid. Make sure it is correct", code="ID error")

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data


class SignUpFacultyForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        exclude = ('User',)
        model = Faculty

    def clean(self):

        # print(self.cleaned_data)
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:

            if password1 != password2:
                raise ValidationError("Make Sure both passwords are same", code="Password doesn't match")

            return self.cleaned_data


class FacultyCoursesForm(forms.ModelForm):

    class Meta:
        model = FacultyCourse
        fields = ['Course', 'Semester']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['Course'].widget.attrs['class'] = "browser-default"


class StudentCoursesForm(forms.ModelForm):

    class Meta:
        model = StudentCourse
        fields = ['Course', 'Semester']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['Course'].widget.attrs['class'] = "browser-default"