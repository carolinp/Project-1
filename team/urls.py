from django.conf.urls import patterns, url

from team import views

urlpatterns = patterns('',

    url(r'^$', 'team.views.home', name='home'),
)
