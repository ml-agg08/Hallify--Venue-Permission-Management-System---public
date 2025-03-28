from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Security(models.Model):

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name='security_profile',on_delete=models.CASCADE)


