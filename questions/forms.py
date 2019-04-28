from django import forms

from questions.models import Answer

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    exclude = []
    widgets = {
      'answer' : forms.Textarea(attrs={'id': 'answer'}),
    }
