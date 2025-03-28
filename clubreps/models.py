from django.db import models
from django.contrib.auth.models import User
from club.models import Clubs
# Create your models here.

class ClubReps(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    BRANCH_CHOICES=(('CSE','Computer Science and Engineering'),('ECE','Electronics and Communication Engineering'),('EEE','Electrical and Electronics Engineering'),('ER','Electrical and Computer Science Engineering'),('ME','Mechanical Engineering'),('CE','Civil Engineering'),("AR","B.ARCH"))

    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,null=True)
    branch=models.CharField(choices=BRANCH_CHOICES,default='CSE',max_length=3)
    batch=models.CharField(max_length=5)

    YEAR_CHOICES=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    year=models.IntegerField(choices=YEAR_CHOICES,default=3)
    admno=models.IntegerField()
    email=models.EmailField(default="hallify@gmail.com")
    user=models.OneToOneField(User,related_name='clubrep_profile',on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    club=models.OneToOneField(Clubs,related_name='clubrep',on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname