from django.forms import ModelForm
from django import forms

from .models import Question, Choice


class SurveyForm(forms.Form):
    # Contact Information Questions
    # First Name
    q1 = forms.CharField(
        label=Question.objects.get(question_title__exact="First Name").question,
        max_length=100,
    )
    # Last Name
    q2 = forms.CharField(
        label=Question.objects.get(question_title__exact="Last Name").question,
        max_length=100,
    )
    # Suffix
    q3 = forms.CharField(
        label=Question.objects.get(question_title__exact="Suffix").question,
        max_length=100,
    )
    # Email
    q4 = forms.EmailField(
        label=Question.objects.get(question_title__exact="Email").question,
        max_length=100,
    )
    # Status
    q5 = forms.ModelChoiceField(
        label=Question.objects.get(question_title__exact="Status").question,
        queryset=Choice.objects.filter(question=7).order_by("-position"),
    )
