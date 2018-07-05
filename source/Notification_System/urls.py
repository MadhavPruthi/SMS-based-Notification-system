from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from source.accounts import urls as accounts_urls
from source.query import urls as query_urls

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^query/', include(query_urls)),
    url(r'^main/$', TemplateView.as_view(template_name='accounts/main.html'), name='main'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^check/$', TemplateView.as_view(template_name='accounts/Faculty_Home.html'), name="FacultyHome"),
    ]

