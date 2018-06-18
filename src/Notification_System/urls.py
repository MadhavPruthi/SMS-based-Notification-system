from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from src.accounts import urls as accounts_urls

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^form/$', TemplateView.as_view(template_name='accounts/form.html')),
    url(r'^form/signup$', TemplateView.as_view(template_name='accounts/form.html')),
    url(r'^login/$', TemplateView.as_view(template_name='accounts/loginForm.html')),
    url(r'^signup/$', TemplateView.as_view(template_name='accounts/signupForm.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact/contact_us.html')),
    ]

