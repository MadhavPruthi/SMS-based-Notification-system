from django.contrib.auth.models import User, Group
from django.db import models
import datetime
from source.accounts.models import Course


class Message(models.Model):

    title = models.TextField()
    message = models.TextField()
    SentBy = models.ForeignKey(User, on_delete=models.CASCADE)
    SentFor = models.ForeignKey(Group, on_delete=models.CASCADE)
    DateTime = models.DateTimeField(default=datetime.datetime.now())
    Status = models.CharField(max_length=10)
    Course = models.CharField(max_length=10)

    def get_message_markdown(self):
        return self.message[0:20]

    def __str__(self):
        return self.title[:10] + " - " + str(self.SentBy.username)
