#Each model class subclasses django.db.models.Model
from django.db import models

#import Python's datetime module
import datetime

#import django's timezone utilities
from django.utils import timezone

#model class for question. It has two variables: question_text and publication_date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now
    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

#model class for Choice. It has two variables: choice_text and votes
#each choice is related to a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

