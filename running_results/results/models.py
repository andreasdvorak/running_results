from django.db import models
from django.urls import reverse
import datetime


class Agegroup(models.Model):
    age = models.IntegerField(unique=True)
    agegroupm = models.CharField(max_length=3)
    agegroupw = models.CharField(max_length=3)
    

    class Meta:
        ordering = ("age", "agegroupm", "agegroupw") 


class Distance(models.Model):
    category_choices = [('d', 'distance'), ('t', 'time')]
    sort = models.IntegerField(unique=True)
    min = models.IntegerField()
    max = models.IntegerField()
    name = models.CharField(max_length=40, unique=True)
    category = models.CharField(choices=category_choices, max_length=1)


    def get_absolute_url(self):
        return reverse("results:distance-details", kwargs={"id": self.id})


    # order first for sort and than name
    class Meta:
        ordering = ("sort", "name")


class Event(models.Model):
    date     = models.DateField()
    location = models.CharField(max_length=40)
    website  = models.URLField(null=True, blank=True,max_length=200)
    note     = models.TextField(null=True, blank=True)
 

    def get_absolute_url(self):
        return reverse("results:events-detail", kwargs={"id": self.id}) #f"/user/{self.id}/" # app_name::name in urls.py


    # order first the lastest date and than location
    class Meta:
        ordering = ("-date", "location") 


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year-10

class Member(models.Model):
    sex_choices = [('w', 'female'), ('m', 'male')]
    lastname      = models.CharField(max_length=40)
    firstname     = models.CharField(max_length=40)
    sex           = models.CharField(max_length=1, choices=sex_choices)
    year_of_birth = models.IntegerField(default=current_year)
 
    # order first the lastest date and than location
    class Meta:
        ordering = ("-lastname", "firstname", "year_of_birth") 


class Result(models.Model):
    distance_id = models.ForeignKey(Distance, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    agegroup_id = models.ForeignKey(Agegroup, on_delete=models.CASCADE)
    result_value = models.IntegerField()


    def get_absolute_url(self):
        return reverse("results:result-detail", kwargs={"id": self.id})


    class Meta:
        ordering = ("result_value", "distance_id")