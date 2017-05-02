import os

from django.conf import settings
from rest_framework.pagination import PageNumberPagination

def paginated_queryset(queryset,request):
	"""Return paginated result of queryset"""
	paginator=PageNumberPagination()
	paginator.page_size=settings.REST_FRAMEWORK['PAGE_SIZE']
	result_page=paginator.paginated_queryset(queryset,request)
	return (paginator,result_page)