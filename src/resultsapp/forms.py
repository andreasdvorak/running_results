"""Module to create forms"""

from django import forms
from .models import Event, ResultDistance


class EventsForm(forms.ModelForm):
    """Form to create events

    Args:
        forms (_type_): _description_
    """
    date = forms.DateField(label='Date', input_formats=['%d.%m.%Y'],
                           widget=forms.TextInput(attrs={"placeholder": "30.10.2020"}))
    location = forms.CharField(label='Location of event', max_length=200,
                               widget=forms.TextInput(attrs={"placeholder": "Ort", 'size': '40'}))
    website = forms.CharField(required=False, label="Website", max_length=200,
                              widget=forms.TextInput(attrs={'size': '40'}))
    notes = forms.CharField(required=False, label="Note", max_length=200, widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        """Define fields to show
        """
        model = Event
        fields = [
            'date',
            'location',
            'website',
            'notes',
        ]


class ResultDistanceForm(forms.ModelForm):
    """Form to create results for distances

    Args:
        forms (_type_): _description_
    """

    class Meta:
        """Define to exclude age_group
        """
        model = ResultDistance
        exclude = ['age_group']
