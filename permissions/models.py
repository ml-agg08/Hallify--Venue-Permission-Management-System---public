from django.db import models
from club.models import Clubs
from venue.models import Venue
from Faculty.models import Faculty
# Create your models here.

class Permission(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)

    venue_name=models.ForeignKey(Venue,on_delete=models.CASCADE,related_name='permissions',null=True)
    event_name=models.CharField(max_length=100,null=True)
    event_description=models.TextField(max_length=500,null=True)
    date_start=models.DateField(null=True)
    date_end=models.DateField(null=True)
    time_start=models.TimeField(null=True)
    time_end=models.TimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(Clubs,on_delete=models.CASCADE,related_name='permissions',null=True,blank=True) #set_null idk refer later.
    fac_owner=models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='permissions',null=True,blank=True)
    fc_tag=models.CharField(default='no')
    off_tag=models.CharField(default='no')
    vfc_tag=models.CharField(default='no')
    scy_tag=models.CharField(default='no')
    