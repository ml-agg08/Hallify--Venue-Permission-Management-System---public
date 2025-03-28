from django.forms import ModelForm
from . models import VenueFacultyStaff
from venue.models import Venue

class VFSForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(VFSForm, self).__init__(*args, **kwargs)  
        self.fields['venue'].queryset = Venue.objects.filter(venue_type='DP')

    class Meta:
        model = VenueFacultyStaff
        fields = ['firstname', 'lastname', 'department','email','venue']