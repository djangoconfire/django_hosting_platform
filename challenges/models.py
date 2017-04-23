from django.db import models
from base.models mport (TimeStampedModel,)


class Challenge(TimeStampedModel):
	title     				= models.CharField(max_length=200)
	short_desc				= models.TextField(null=True,blank=True)
	desc            		= models.TextField(null=True,blank=True)
	terms_nd_conditions		= models.TextField(null=True,blank=True)
	submission_guidelines	= models,TextField(null=True,blank=True)
	evaluation_details		= models.TextField(null=True,blank=True)
	image					= models.ImageField(upload_to="logos",
												null=True,blank=True,verbose_name="Logo")
	start_date				= models.DateTimeField(null=True,blank=True,verbose_name="start_date(UTC)")
	end_date				= models.DateTimeField(null=True,blank=True,verbose_name="end_date(UTC)")
	published				= models.BooleanField(default=False,verbose_name="Publicly Available")
	enable_form				= models.BooleanField(default=False)
	anonymous_leaderboard	= models.BooleanField(default=False)

	class Meta:
		app_label="challenges"
		