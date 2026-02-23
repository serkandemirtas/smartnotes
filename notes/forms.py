from django  import forms
from django.core.exceptions import ValidationError
from .models import Notes

from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        labels = {
            'text': 'Write your thoughts here:'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if  len(title) < 10:
            raise ValidationError('The title must be at least 10 characters')
        return title