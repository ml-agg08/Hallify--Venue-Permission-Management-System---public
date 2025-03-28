from django.db import models

# Create your models here.

class Clubs(models.Model):
    club_name=models.CharField(max_length=60,null=True)       
    def __str__(self):
        return self.club_name