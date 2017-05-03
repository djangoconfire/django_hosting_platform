from rest_framework import permissions,status
from rest_framework.response import Response 
from rest_framework.decorators import (api_view,
										permission_classes,)

from django.contrib.auth import logout

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def disable_user(request):
	user=request.user
	user.is_active=False
	user.save()
	logout(request)
	return Response(status=status.HTTP_200_OK)