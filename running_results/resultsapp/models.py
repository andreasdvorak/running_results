from django.db import models
from django.urls import reverse
import datetime


class Agegroup(models.Model):
    age = models.IntegerField(unique=True)
    agegroupm = models.CharField(max_length=3)
    agegroupw = models.CharField(max_length=3)
    

    # show agegroupm of Distance object (x)
    def __str__(self):
        return f"{self.age}"


    class Meta:
        ordering = ("age", "agegroupm", "agegroupw") 


class Distance(models.Model):
    category_choices = [('d', 'distance'), ('t', 'time')]
    sort = models.IntegerField(unique=True)
    min = models.IntegerField()
    max = models.IntegerField()
    name = models.CharField(max_length=40, unique=True)
    category = models.CharField(choices=category_choices, max_length=1)


    # show name instead of Distance object (x)
    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        return reverse("resultsapp:distance-details", kwargs={"id": self.id})


    # order first for sort and than name
    class Meta:
        ordering = ("sort", "name")


class Event(models.Model):
    date     = models.DateField()
    location = models.CharField(max_length=40)
    website  = models.URLField(null=True, blank=True,max_length=200)
    note     = models.TextField(null=True, blank=True)
 

    # show date and location instead of Distance object (x)
    def __str__(self):
        return f"{self.date} {self.location}"


    def get_absolute_url(self):
        return reverse("resultsapp:events-detail", kwargs={"id": self.id}) #f"/user/{self.id}/" # app_name::name in urls.py


    # order first the lastest date and than location
    class Meta:
        ordering = ("-date", "location") 


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year-10

class Member(models.Model):
    sex_choices = [('w', 'female'), ('m', 'male')]
    firstname     = models.CharField(max_length=40)
    lastname      = models.CharField(max_length=40)
    sex           = models.CharField(max_length=1, choices=sex_choices)
    year_of_birth = models.IntegerField(default=current_year)


    # values to show instead of istance object (x)
    def __str__(self):
        return f"{self.lastname}, {self.firstname} {self.sex} {self.year_of_birth}"

    # order first the lastest date and than location
    class Meta:
        ordering = ("-lastname", "firstname", "year_of_birth") 


class Result(models.Model):
    distance_id = models.ForeignKey(Distance, on_delete=models.CASCADE, verbose_name = "distance")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name = "event")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name = "member")
    agegroup = models.CharField(max_length=3)
    result_value = models.TimeField(auto_now=False, auto_now_add=False, default="00:00:00", help_text = "hh:mm:ss")


    def get_absolute_url(self):
        return reverse("app:result-detail", kwargs={"id": self.id})


    class Meta:
        ordering = ("agegroup", "distance_id", "result_value")