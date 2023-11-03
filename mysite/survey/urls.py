from django.urls import path
from . import views

app_name = "survey"
urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.get_survey, name="form"),
    path("detail", views.detail, name="detail"),
]
