from django import forms
from .models import Event, Result


class EventsForm(forms.ModelForm):
    date = forms.DateField(label='Date', input_formats=['%d.%m.%Y'],
                           widget=forms.TextInput(attrs={"placeholder": "30.10.2020"}))
    location = forms.CharField(label='Location of event', max_length=200,
                               widget=forms.TextInput(attrs={"placeholder": "Ort", 'size': '40'}))
    website = forms.CharField(required=False, label="Website", max_length=200,
                              widget=forms.TextInput(attrs={'size': '40'}))
    notes = forms.CharField(required=False, label="Note", max_length=200, widget=forms.TextInput(attrs={'size': '40'}))

    class Meta:
        model = Event
        fields = [
            'date',
            'location',
            'website',
            'notes',
        ]


class ResultForm(forms.ModelForm):

    # do not show agegroup
    class Meta:
        model = Result
        exclude = ['agegroup']
