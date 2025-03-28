from django.forms import ModelForm

from . models import ClubReps

class CRForm(ModelForm):
    class Meta:
        model=ClubReps
        fields=['firstname', 'lastname','phone', 'branch', 'batch', 'year', 'admno','email','club']
