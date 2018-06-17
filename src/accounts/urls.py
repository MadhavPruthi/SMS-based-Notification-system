from django.conf.urls import url
from src.accounts.views import LoginView

app_name = 'accounts'

urlpatterns = [

    url(r'^login/$', LoginView , name="login"),
]