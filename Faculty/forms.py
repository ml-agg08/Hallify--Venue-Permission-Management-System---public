from django.forms import ModelForm
from . models import Faculty

class FacultyForm(ModelForm):
    class Meta:
        model=Faculty
        fields=["firstname","lastname","department","phone","email"]

