from django.db import models
from django.contrib.auth.models import User
from venue.models import Venue
# Create your models here.

class VenueFacultyStaff(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    department=models.CharField(max_length=30)
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name="venuefacultystaff_profile",on_delete=models.CASCADE)
    venue=models.OneToOneField(Venue,related_name="venuefacultystaff",on_delete=models.CASCADE)