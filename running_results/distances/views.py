from django.shortcuts import render, get_object_or_404, redirect

from .helper import Helper
from .models import Distance


def distance_detail_view(request, id):
    obj = get_object_or_404(Distance, id=id)
    obj.min = Helper.convert_from_seconds(obj.min)
    obj.max = Helper.convert_from_seconds(obj.max)
    context = {
        "object": obj
    }
    return render(request, "distances/distance_detail.html", context)


def distances_list_view(request):
    queryset = Distance.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "distances/distances_list.html", context)