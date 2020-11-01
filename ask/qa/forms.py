from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Answer, Question


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(Question.objects)

    def save(self):
        answer = Answer(**self.cleaned_data)
        return answer


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        user = get_object_or_404(User, {
            'username': self.cleaned_data['username'],
            'password': self.cleaned_data['password']
        })
        return user
