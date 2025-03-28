from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Faculty(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    department=models.CharField(max_length=50)
    email=models.EmailField()
    user=models.OneToOneField(User,related_name='faculty_profile',on_delete=models.CASCADE)

    def __str__(self):
        return Faculty.firstname


