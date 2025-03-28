from django import forms

from . models import Permission
from venue.models import Venue

class PermissionForm(forms.ModelForm):

    date_start=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    date_end=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time_start=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    time_end=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
        
    class Meta:
        model=Permission
        fields=['venue_name','event_name','event_description','date_start','date_end','time_start','time_end']


class ClashInfoForm(forms.Form):
    date_start=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),required=False)
    date_end=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),required=False)
    venue_name = forms.ModelChoiceField(
        queryset=Venue.objects.all(),  
        empty_label="Select a venue",   
        to_field_name="venue_name",
        required=False
    )
