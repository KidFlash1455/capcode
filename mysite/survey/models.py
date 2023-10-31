from django.db import models
from django.contrib.auth.models import User  # new


class Question(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return self.reponse_text
