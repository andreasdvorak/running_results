from django import forms

from .models import User

class UserForm(forms.ModelForm):
    firstname   = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "FIRSTNAME"}))
    lastname    = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "LASTNAME"}))
    username    = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "USERNAME"}))
    email       = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "EMAIL"}))
    password    = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "PASSWORD"}))
    role        = forms.CharField(label='', 
                  widget=forms.TextInput(attrs={"placeholder": "ROLE"}))
    
    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'username',
            'email',
            'password',
            'role'
        ]   
