from django.contrib.auth.models import User, Group
from django.db import models


class Message(models.Model):

    title = models.TextField()
    SentBy = models.ForeignKey(User, on_delete=models.CASCADE)
    SentFor = models.ForeignKey(Group, on_delete=models.CASCADE)
    DateTime = models.DateTimeField(auto_now=True)
    Status = models.CharField(max_length=10)

    def get_title_markdown(self):
        return self.title[0:20]
