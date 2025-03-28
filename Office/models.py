from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Office(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name='office_profile',on_delete=models.CASCADE)


