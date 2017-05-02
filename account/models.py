from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.modls import User
from django.dispatch import reciever
from base.models import TimeStampedModel

class UserStatus(TimeStampedModel):
	"""
		Model representing status of user being invited
		by other user to host/participate in competition.

		There are four ststus
		-Unknown
		-Denied
		-Accepted
		-Pending
	"""

	UNKNOWN='unknown'
	DENIED='denied'
	ACCEPTED='accepted'
	PENDING='pending'
	
	name	= models.CharField(max_length=100)
	status  = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name

	
	class Meta:
		app_label='account'


class Connection(TimeStampedModel):
	"""
		MOdel to store the connection
	"""
	
	name	= models.TextField()

	class Meta:
		app_label='account'
		db_table='connection'

class UserConnection(TimeStampedModel):
	"""
		Model to relate the connection to a particular user
	"""
	
	connection  	= models.ForeignKey(Connection)
	user 			= models.ForeignKey(User)

	class Meta:
		app_label='account'
		db_table='user_connection'


class UserProfile(TimeStampedModel):
	"""
		Model to store th user parofile
	"""
	
	user  			 = models.OneToOneField(User)
	connection       = models.CharField(max_length=200)
	contact_number   = models.CharField(max_length=10,blank=False,null=True)

	def __unicode__(self):
		return '{}'.format(self.user)


	class Meta:
		app_label='account'
		db_table='user_profile'



@reciever(post_save,sender=User)
def create_user_profile(sender,instance,cretaed,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)

					
