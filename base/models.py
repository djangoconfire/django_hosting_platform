from django.db import models

class TimeStampedModel(models.Model):
	'''
	A base class model that provides 
	self managed created_at modified_at fields.
	'''
	cretaed_at	= models.DateTimeField(auto_now_add=True)
	modified_at	= models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True
		app_label='base'



