from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):

    QuestionTitle = models.TextField()
    AskedAt = models.DateTimeField(auto_now=True)
    IsAnswered = models.BooleanField(default=False)
    CreatedFor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    QueriedBy = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.QuestionTitle


class Answer(models.Model):

    Question = models.OneToOneField(Question)
    AnswerTitle = models.TextField()
    AnsweredAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.AnswerTitle