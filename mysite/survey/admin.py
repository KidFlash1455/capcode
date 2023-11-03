from django.contrib import admin

from .models import Question, Choice


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["pk", "question", "question_title", "question_type"]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question", "choice", "position"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
