from background_task import background
from datetime import datetime
from django.contrib.auth.models import User
from django.core import serializers
from django.utils.timezone import make_aware
from source.Notification_System.settings import client
from source.accounts.models import Student, Faculty


def messageAPINexmo(sender , receiver, message):

    response = client.send_message({'from': sender, 'to': receiver, 'text': message})
    response = response['messages'][0]

    if response['status'] == '0':
        return "SENT"
    else:
        return "ERROR"


@background(schedule=2)
def messagesendingsetup(message):

    for obj in serializers.deserialize('json', message):
        message = obj.object

    group = message.SentFor
    users = User.objects.filter(groups=group)
    SentBy = message.SentBy
    title = message.title
    Message = message.message
    course = message.Course
    time = (message.DateTime - make_aware(datetime.now())).seconds
    print(time, users, SentBy)

    if users:
        for user in users:
            sendmessage(
                title,
                Message,
                str(Student.objects.get(User=user).ContactNumber),
                str(Faculty.objects.get(FacultyID=SentBy).ContactNumber),
                course,
                schedule=time
            )


@background(schedule=30)
def sendmessage(title, message, ContactNumber, SentByContactNumber, course):

    string = title + "\n" + "Course- " + course + "\n" + message
    response = messageAPINexmo(
        sender= SentByContactNumber,
        receiver=ContactNumber,
        message=string
    )

    print(response)

