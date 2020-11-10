from django.db import models
from django.urls import reverse

class Agegroup(models.Model):
    age = models.IntegerField(unique=True)
    agegroupm = models.CharField(max_length=3)
    agegroupw = models.CharField(max_length=3)
    

    class Meta:
        ordering = ("age", "agegroupm", "agegroupw") 
