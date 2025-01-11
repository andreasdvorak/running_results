import datetime
import logging
from django.db import models
from django.urls import reverse

logger = logging.getLogger('console_file')


class AgeGroup(models.Model):
    age = models.IntegerField(unique=True)
    age_group_m = models.CharField(max_length=3)
    age_group_w = models.CharField(max_length=3)

    # show age_group_m of Discipline object (x)
    def __str__(self):
        return f"{self.age}"

    class Meta:
        ordering = ("age", "age_group_m", "age_group_w")


class Club(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    allow_public_record = models.BooleanField(default=False)

    # show name instead of Club object (x)
    def __str__(self):
        return f"{self.name}"


class DisciplineDistance(models.Model):
    sort = models.IntegerField(unique=True)
    min = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, help_text="hh:mm:ss", null=True)
    max = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, help_text="hh:mm:ss", null=True)
    name = models.CharField(max_length=40, unique=True)

    # show name instead of DisciplineDistance object (x)
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("resultsapp:discipline_distance_details", kwargs={"id": self.id})

    # order first for sort and than name
    class Meta:
        ordering = ("sort", "name")


class DisciplineTime(models.Model):
    sort = models.IntegerField(unique=True)
    min = models.IntegerField(null=True, blank=True)
    max = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40, unique=True)

    # show name instead of DisciplineTime object (x)
    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("resultsapp:discipline_time_details", kwargs={"id": self.id})

    # order first for sort and than name
    class Meta:
        ordering = ("sort", "name")


class Event(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=40)
    website = models.URLField(null=True, blank=True, max_length=200)
    note = models.TextField(null=True, blank=True)

    # show date and location instead of Discipline object (x)
    def __str__(self):
        return f"{self.date} {self.location}"

    def get_absolute_url(self):
        # f"/user/{self.id}/" # app_name::name in urls.py
        return reverse("resultsapp:events-detail", kwargs={"id": self.id})

    # order first the latest date and than location
    class Meta:
        ordering = ("-date", "location")


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year-10


class Member(models.Model):
    sex_choices = [('w', 'female'), ('m', 'male')]
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=sex_choices)
    year_of_birth = models.IntegerField(default=current_year)

    # values to show instead of instance object (x)
    def __str__(self):
        return f"{self.lastname}, {self.firstname} {self.sex} {self.year_of_birth}"

    # order first the latest date and than location
    class Meta:
        ordering = ("-lastname", "firstname", "year_of_birth")


# results for discipline as distance
class ResultDistance(models.Model):
    discipline_id = models.ForeignKey(
        DisciplineDistance, on_delete=models.CASCADE, verbose_name="discipline")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="event")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="member")
    age_group = models.CharField(max_length=3)
    result_value = models.TimeField(
        auto_now=False, auto_now_add=False, default="00:00:00", help_text="hh:mm:ss")

    def get_absolute_url(self):
        return reverse("app:result-detail", kwargs={"id": self.id})

    class Meta:
        ordering = ("age_group", "discipline_id", "result_value")


# results for discipline as time
class ResultTime(models.Model):
    discipline_id = models.ForeignKey(
        DisciplineTime, on_delete=models.CASCADE, verbose_name="discipline")
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="event")
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="member")
    age_group = models.CharField(max_length=3)
    result_value = models.IntegerField(help_text="Meter")

    def get_absolute_url(self):
        return reverse("app:result-detail", kwargs={"id": self.id})

    class Meta:
        ordering = ("age_group", "discipline_id", "result_value")
