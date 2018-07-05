from django.conf.urls import url
from .views import CreateQueryView

urlpatterns = [
    url(r'^create/$', CreateQueryView, name="createquery"),
]