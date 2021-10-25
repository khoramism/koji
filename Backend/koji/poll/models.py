from django.db import models
import datetime 
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    q_creator = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='q_creator')
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    

class Vote(models.Model):
    vote_date = models.DateTimeField('vote_dated')
    voter = models.ForeignKey("account.UserProfile", on_delete=models.CASCADE, related_name='q_voter')
    choice = models.ManyToManyField(Choice)
    