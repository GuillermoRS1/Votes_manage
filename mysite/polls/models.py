import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# This class will be for information on the one question
class Question(models.Model):
    # Save the text of the question
    question_text = models.CharField(max_length=200)
    # Save the date on which the question was posted
    pub_date = models.DateTimeField('date published')

    # To return a more readable representation of the result
    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    # To see if the question was created less than a day ago or more than a day ago
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# This class will be for the options that will have a question
class Choice(models.Model):
    # To identify the answers to the question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Save the text of the options
    choice_text = models.CharField(max_length=200)
    # Save the result of the vote
    votes = models.IntegerField(default=0)

    # To return a more readable representation of the result
    def __str__(self):
        return self.choice_text