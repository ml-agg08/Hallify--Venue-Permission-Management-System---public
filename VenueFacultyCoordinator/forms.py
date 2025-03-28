from django.forms import ModelForm

from . models import VenueFacultyCoordinator

class VFCForm(ModelForm):
    class Meta:
        model=VenueFacultyCoordinator
        fields=['firstname','lastname','department','venue','email']