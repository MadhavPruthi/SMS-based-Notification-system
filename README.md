# SMS-based-Notification-system
Notification-System is a project which will help faculty to intimidate students about any important information like Schedule Changes, any upcoming seminar and other information. This information will be shared through SMS. Through other platforms like whatsapp, sometimes information got missed due to network gliches or any else reason, due to which we adopted SMS for message sharing.
Also, Additional functionality of asking queries has also been added. With this, Students can ask their queries to their respective teachers easily

# Technologies Used

This is built on django framework along with HTML, CSS and Bootstrap as front-end framework. At some instances, AJAX is also used to provide the touch of asynchronous manner.
To handle the message queuing, Django-background-tasks has been used which schedule the messages according to time and date set by Faculty.
Nexmo has been used as SMS API service.

# Setup Your Environment

Setup virtualenv by running command:
```
virtualenv -p python3 VirtualEnvNotification
```
Next activate it through following command:
```
cd VirtualEnvNotification
cd Scripts/activate
```
Install all the dependencies:
```
pip install -r requirements.txt
```
Now we are ready to boot the server
Run following command to run the localhost WSGI server of Django:
```
python manage.py runserver
```
You also have to run following command to also boot the background server:
```
python manage.py process_tasks
```
And we are done!

# Preview of the project

> Home Page

![Home Page](https://user-images.githubusercontent.com/37483320/43248981-1a411ec0-90d7-11e8-817e-bf905db16b0c.png)

> Login Page

![Login Page](https://user-images.githubusercontent.com/37483320/43248983-1a94bc74-90d7-11e8-9737-37ad9e116266.png)

> Faculty/Staff Profile Page

![Faculty/Staff Profile Page](https://user-images.githubusercontent.com/37483320/43248979-19d9e70a-90d7-11e8-8564-3d344707de5f.png)

> Message Creation Page for Staff Access Only

![Message Creation Page for Staff Access Only](https://user-images.githubusercontent.com/37483320/43249680-f3efacee-90d8-11e8-8bb3-b80afffc3343.png)

> Student Dashboard

![Student Dashboard](https://user-images.githubusercontent.com/37483320/43248984-1ad3a3b2-90d7-11e8-837a-0c541a767932.png)
