from django import forms
from source.query.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = "__all__"
