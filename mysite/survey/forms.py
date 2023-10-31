from django.forms import ModelForm
from django import forms
from .models import Question, Response


class SubmitForm(ModelForm):
    question_text = forms.TextInput()
    question_type = forms.TextInput()

    class Meta:
        model = Question
        fields = ["question_text", "question_type"]
