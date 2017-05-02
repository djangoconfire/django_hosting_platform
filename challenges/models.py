from django.db import models
from base.models import (TimeStampedModel,)
from django.utils import timezone


class Challenge(TimeStampedModel):
    title                   = models.CharField(max_length=200)
    short_desc              = models.TextField(null=True,blank=True)
    desc                    = models.TextField(null=True,blank=True)
    terms_nd_conditions     = models.TextField(null=True,blank=True)
    submission_guidelines   = models.TextField(null=True,blank=True)
    evaluation_details      = models.TextField(null=True,blank=True)
    creator                 = models.ForeignKey('hosts.ChallengeHostTeam', related_name='challenge_creator')
    image                   = models.ImageField(upload_to="logos",
                                                null=True,blank=True,verbose_name="Logo")
    start_date              = models.DateTimeField(null=True,blank=True,verbose_name="start_date(UTC)")
    end_date                = models.DateTimeField(null=True,blank=True,verbose_name="end_date(UTC)")
    published               = models.BooleanField(default=False,verbose_name="Publicly Available")
    enable_forum            = models.BooleanField(default=False)
    anonymous_leaderboard   = models.BooleanField(default=False)

    class Meta:
        app_label="challenges"
        db_table="challenge"

    def __unicode__(self):
        """ Return title of the chaleenge"""
        return self.title

    def get_image_url(self):
        """ Return url of the logo of the challenge"""
        if self.image:
            return self.image.url
        return None
        
    def start_date(self):
        """ Return start date of the challenge"""
        return self.start_date

    def end_date(self):
        """ Return end date of the challenge"""
        return self.end_date

    @property
    def is_active(self):
        """ Return if challenge is active or not""" 
        if self.start_date<timezone.now() and self.end_date>timezone.now():
            return True
        return False        
                            
