from django.db import models
from django.contrib.auth.models import User
from club.models import Clubs
# Create your models here.

class FacultyCoordinator(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name='facultycoordinator_profile',on_delete=models.CASCADE)
    club=models.OneToOneField(Clubs,related_name='facultycoordinator',on_delete=models.CASCADE,null=True)

