from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Response
from .forms import SubmitForm


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "survey/detail.html", {"question": question})


def upload(request):
    if request.POST:
        form = SubmitForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "survey/form.html", {"form": SubmitForm})
