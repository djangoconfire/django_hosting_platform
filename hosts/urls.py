from django.conf.urls import url 

from . import views

urlpatterns=[
	url(r'^challenge_host_team/$',views.ChallengeHostTeamList,name='challenge_host_team_list')





]