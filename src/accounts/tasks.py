import nexmo
from background_task import background
from django.contrib.auth.models import User
from src.Notification_System import settings


@background(schedule=60)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    user.email_user('Here is a notification', 'You have been notified', from_email='madhavpruthi0@gmail.com')


@background(schedule=120)
def send_message(user_id, sender, receiver, message):

    client = nexmo.Client(key=settings.KEY , secret=settings.SECRET)
    string = str(message)
    response = client.send_message({'from': sender, 'to': receiver, 'text': string})
    response = response['messages'][0]

    if response['status'] == '0':
        print("SENT")
    else:
        print("ERROR")