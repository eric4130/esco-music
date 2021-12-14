from django import forms
from .models import BandProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = BandProfile
        fields = ['bandName', 'bandSummary', 'bandImage' ]
        labels = {'bandName':'Enter a band name:', 'bandSummary':'Enter a description of your band:', 'bandImage':'Upload a band picture:'}
