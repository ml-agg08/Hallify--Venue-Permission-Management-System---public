from django.forms import ModelForm
from . models import Security

class SecurityForm(ModelForm):
    class Meta:
        model=Security
        fields=["firstname","lastname","phone","email"]
