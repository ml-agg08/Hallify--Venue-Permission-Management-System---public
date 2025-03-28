from django.db import models

# Create your models here.

class Venue(models.Model):

    general='GN'
    dept='DP'
    room='CL'
    venue_types=[
        (general,"General Venue"),
        (dept,"Department Venue"),
        (room,"Class Room")
    ]  

    venue_name=models.CharField(max_length=50)
    venue_type=models.CharField(choices=venue_types,max_length=2,default=general)
    def __str__(self):
        return self.venue_name