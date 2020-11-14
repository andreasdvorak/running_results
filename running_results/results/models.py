from django.db import models
from django.urls import reverse
from agegroups.models import Agegroup
from distances.models import Distance
from events.models import Event
from member.models import Member


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