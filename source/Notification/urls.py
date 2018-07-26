from django.conf.urls import url
from source.Notification import views

app_name = "notification"

urlpatterns = [
    url(r'create/$', views.CreateNotificationView, name="CreateNotification"),
]