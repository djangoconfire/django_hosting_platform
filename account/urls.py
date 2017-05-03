from django.conf.urls import url

from . import views

urlpatterns=[

	url('user/disable$',views.disable_user,name="disable_user")

]