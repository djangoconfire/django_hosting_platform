from rest_framework import permissions, status
from rest_framework.decorators import (api_view,
										authentication_classes,
										permission_classes,)
from rest_framework.response import Response 
from models import (ChallengeHost,
					ChallengeHostTeam,)

from .serializers import (ChallengeHostSerializer,
						  ChallengeHostTeamSerializer,
						  HostTeamDetailSerializer,)
from base.utils import paginated_queryset	

@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticated))
def ChallengeHostTeamList(request):
	if request.method:
		challenge_host_team_ids=ChallengeHost.objects.filter(user=request.user)\
													 .values_list('team_name',flat=True)
		challenge_host_teams=ChallengeHostTeam.objects.filter(id__in=challenge_host_team_ids)
		paginator,result_page=paginated_queryset(challenge_host_teams,request)
		serializer=HostTeamDetailSerializer(result_page,many=True)
		reaponse_data=serializer.data 
		return paginator.get_paginated_response(reaponse_data)

	
	elif request.method=='POST':
		serializer=ChallengeHostTeamSerializer(data=request.data,context={'request':request})

		if serializer.is_valid():
			serializer.save()
			reaponse_data=serializer.data
			return Response(reaponse_data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		






