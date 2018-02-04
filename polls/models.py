#Each model class subclasses django.db.models.Model
from django.db import models

#model class for question. It has two variables: question_text and publication_date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')

#model class for Choice. It has two variables: choice_text and votes
#each choice is related to a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

