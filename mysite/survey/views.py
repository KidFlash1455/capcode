from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question, Response
from django.http import HttpResponseRedirect
from .forms import SurveyForm

# from .forms import SubmitForm


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "survey/detail.html", {"question": question})


# def upload(request):
#     if request.POST:
#         form = SubmitForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, "survey/form.html", {"form": SubmitForm})


def get_survey(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SurveyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SurveyForm()

    return render(request, "survey/survey.html", {"form": form})


def detail(request):
    question = Question.objects.all()
    return render(request, "survey/detail.html", {"question": question})


def index(request):
    return HttpResponse("Index!")
