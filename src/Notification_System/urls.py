from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$', TemplateView.as_view(template_name='accounts/form.html')),
    url(r'^login/$', TemplateView.as_view(template_name='accounts/loginForm.html')),
]
