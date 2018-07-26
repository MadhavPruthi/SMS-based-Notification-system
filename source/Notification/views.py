from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.utils.timezone import make_aware
from source.Notification.models import Message
from source.accounts.models import Faculty, Course
from .tasks import messagesendingsetup
from django.core import serializers
from source.Notification.forms import clean


@login_required()
def CreateNotificationView(request):

    Courses = Course.objects.filter(faculty__User=get_user(request))
    context = {
        "Courses" : Courses,
    }
    if request.method == "POST":

        values = request.POST

        message = Message()

        message.SentBy = get_user(request)
        message.SentFor = Group.objects.get(name=values['group1'])

        message.title = values['title']
        message.message = values['message']
        message.Course = values['Course']

        DateTime = values['date'] + " " + values['time']
        message.DateTime = make_aware(datetime.datetime.strptime(DateTime, '%b %d, %Y %H:%M'))

        if clean(message.DateTime):

            message.save()
            message = serializers.serialize("json", [message])

            messagesendingsetup(message)
            context = {
                "errors": "Message Sent"
            }

        else:
            context = {
                    "errors" : "Date and Time are not correct",
            }


    return render(request, 'notification/NotifSend.html', context)

