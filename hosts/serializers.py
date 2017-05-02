from rest_framework import serializers
from models import (ChallengeHostTeam,
					ChallengeHost,
					)

from django.contrib.auth.models import User

class ChallengeHostTeamSerializer(serializers.ModelSerializer):
	created_by	=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all())

	def __init__(self,*args,**kwargs):
		super(ChallengeHostTeamSerializer,self).__init__(*args,**kwargs)
		context=kwargs.get('context')
		if context:
			request=context.get('request')
			context['data']['created_by']=request.user.username

	class Meta:
		model=ChallengeHostTeam
		fields=['id','team_name','created_by']


class ChallengeHostSerializer(serializers.ModelSerializer):
	status=serializers.ChoiceField(choices=ChallengeHost.STATUS_OPTIONS)
	permissions=serializers.ChoiceField(choices=ChallengeHost.PERMISSION_OPTIONS)
	user=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all())

	def __init__(self,*args,**kwargs):
		super(ChallengeHostSerializer,self).__init__(*args,**kwargs)
		context=kwargs.get('context')
		if context:
			challenge_host_team=context.get('challenge_host_team')
			request=context.get('request')
			context['data']['team_name']=challenge_host_team.pk
			context['data']['user']=request.user.username


	class Meta:
		model=ChallengeHost
		fields=['id','user','team_name','status','permissions']		
		

class HostTeamDetailSerializer(serializers.ModelSerializer):
	members=serializers.SerializerMethodField()
	created_by=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all())
	
	class Meta:
		model=ChallengeHostTeam
		fields=['id','team_name','created_by','members']


	def get_members(self,obj):
		hosts=ChallengeHost.objects.filter(team_name_id=obj.id)
		serializer=ChallengeHostSerializer(hosts,many=True)
		return serializer.data






