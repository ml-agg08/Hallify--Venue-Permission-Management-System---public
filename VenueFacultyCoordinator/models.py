from django.db import models
from django.contrib.auth.models import User
from venue.models import Venue
# Create your models here.

class VenueFacultyCoordinator(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name='venuefacultycoordinator_profile',on_delete=models.CASCADE)
    venue=models.OneToOneField(Venue,related_name='venuefacultycoordinator',on_delete=models.CASCADE,null=True)

