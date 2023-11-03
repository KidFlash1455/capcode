from django.db import models
from django.contrib.auth.models import User  # new
from datetime import date

# class Question(models.Model):
#     QUESTION_TYPES = [
#         ("MC", "Multiple Choice"),
#         ("TF", "Text Field"),
#         ("DF", "Date Field"),
#         ("RB", "Radio Button"),
#     ]
#     question_type = models.CharField(max_length=2, choices=QUESTION_TYPES)
#     question_content = models.TextField(max_length=200, default="Enter Question")

#     # User Input

#     question_multiple_choice =


class Response(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return self.reponse_text


class Question(models.Model):
    question = models.TextField(max_length=200, default="Enter")
    question_title = models.CharField(max_length=200, default="Default")
    QUESTION_TYPES = [
        ("MC", "Multiple Choice"),
        ("TF", "Text Field"),
        ("DF", "Date Field"),
        ("RB", "Radio Button"),
        ("EM", "Email"),
    ]
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, default="MR")

    def __str__(self):
        return self.question


class Text(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    question_textfield = models.TextField(max_length=200, default="Enter Text Here")


class Choice(models.Model):
    # myquestion.choices.all()
    question = models.ForeignKey(
        "Question", related_name="choices", on_delete=models.CASCADE, default="Enter"
    )
    choice = models.TextField("Choice")
    position = models.IntegerField("position")

    def __str__(self):
        return self.choice

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"),
            # no duplicated position per question
            ("question", "position"),
        ]
        ordering = ("position",)
