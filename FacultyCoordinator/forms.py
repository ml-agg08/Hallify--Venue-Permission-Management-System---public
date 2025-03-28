from django.forms import ModelForm

from . models import FacultyCoordinator

class FCForm(ModelForm):
    class Meta:
        model=FacultyCoordinator
        fields=['firstname','lastname','department','club','email']