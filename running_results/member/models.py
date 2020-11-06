from django.db import models
from django.urls import reverse
import datetime

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year-10

class Member(models.Model):
    sex_choices = [('w', 'female'), ('m', 'male')]
    lastname      = models.CharField(max_length=40)
    firistname    = models.CharField(max_length=40)
    sex           = models.CharField(max_length=1, choices=sex_choices)
    year_of_birth = models.IntegerField(default=current_year)
 
    # order first the lastest date and than location
    class Meta:
        ordering = ("-lastname", "firistname", "year_of_birth") 