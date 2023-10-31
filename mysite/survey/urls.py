from django.urls import path
from . import views

app_name = "survey"
urlpatterns = [
    path("form", views.upload, name="form"),
]
