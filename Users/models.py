from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserType(models.Model):
    ClubRep='CR'
    FacultyCoordinator='FC'
    VenueFacultyCoordinator='VFC'
    VenueFacultyStaff='VFS'
    Security='SCY'
    Office='OFF'
    user_type_choices=[
        (ClubRep,'Club Representative'),
        (FacultyCoordinator,'Faculty Coordinator'),
        (VenueFacultyCoordinator,'Venue Faculty Coordinator'),
        (VenueFacultyStaff,"Venue Faculty Staff"),
        (Security,"Security"),
        (Office,"Office Personnel")
    ]
    user=models.OneToOneField(User,related_name='user_type',on_delete=models.CASCADE)
    user_type=models.CharField(choices=user_type_choices,max_length=3,default=ClubRep)

    def __str__(self):
        return self.user_type