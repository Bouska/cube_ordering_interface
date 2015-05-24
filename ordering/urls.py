from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('ordering.views',
    url(r'^$', TemplateView.as_view(template_name="home.haml"), name='home'),
)
