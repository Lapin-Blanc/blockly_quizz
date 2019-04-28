from django import forms

from questions.models import Answer

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    exclude = []
    widgets = {
      'answer' : forms.HiddenInput(attrs={'id': 'answer',}),
      'question' : forms.HiddenInput(),
      'exam' : forms.HiddenInput(),
      'answered' : forms.HiddenInput(),
    }
