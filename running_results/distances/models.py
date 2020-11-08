from django.db import models
from django.urls import reverse

class Distances(models.Model):
    category_choices = [('d', 'distance'), ('t', 'time')]
    sort = models.IntegerField(unique=True)
    min = models.IntegerField()
    max = models.IntegerField()
    name = models.CharField(max_length=40, unique=True)
    category = models.CharField(choices=category_choices, max_length=1)

    # order first for sort and than name
    class Meta:
        ordering = ("sort", "name")