from django import forms

class QueryForm(forms.Form):
    QuestionTitle = forms.CharField(max_length=30,widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Enter title here'
            }
        ))
    Query_To = forms.CharField(max_length=254,widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',

            }
        ))
    Message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: blue;'}),


    )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(QueryForm, self).clean()
        Title = cleaned_data.get('Title')
        To = cleaned_data.get('To')
        message = cleaned_data.get('message')
        if not Title and not To and not message:
            raise forms.ValidationError('You have to write something!')