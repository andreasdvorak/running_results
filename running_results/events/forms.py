from django import forms

from .models import Event

class EventsForm(forms.ModelForm):
    date     = forms.DateField(label='Datum',input_formats=['%d.%m.%Y'],widget=forms.TextInput(attrs={"placeholder": "30.10.2020"}))
    location = forms.CharField(label='Veranstaltungsort', 
                 widget=forms.TextInput(attrs={"placeholder": "Ort"}))
    
    class Meta:
        model = Event
        fields = [
            'date',
            'location'
        ]   
