from django import forms

from .models import Event

class EventsForm(forms.ModelForm):
    date     = forms.DateField(label='Datum',input_formats=['%d.%m.%Y'],widget=forms.TextInput(attrs={"placeholder": "30.10.2020"}))
    location = forms.CharField(label='Veranstaltungsort', max_length=200, widget=forms.TextInput(attrs={"placeholder": "Ort", 'size':'40'}))
    website  = forms.CharField(required=False, label="Webseite", max_length=200, widget=forms.TextInput(attrs={'size':'40'}))
    notes    = forms.CharField(required=False, label="Bemerkung", max_length=200, widget=forms.TextInput(attrs={'size':'40'}))
    
    class Meta:
        model = Event
        fields = [
            'date',
            'location',
            'website',
            'notes',
        ]   
