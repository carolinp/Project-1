from django.conf.urls import patterns, url

from team import views

urlpatterns = patterns('',

    url(r'^$', 'team.views.home', name='team_home'),
    #url(r'^player/$', 'team.views.player', name='team_player_list'),
    url(r'^roster/$', 'team.views.roster', name='team_roster'),
    url(r'^player/(?P<pk>\d+)$', 'team.views.player', name='team_player'),
)
