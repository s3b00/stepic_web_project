from django import forms
from django.contrib.auth.models import User

from .models import Answer, Question


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(Question.objects)
    author = forms.ModelChoiceField(User.objects)

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
