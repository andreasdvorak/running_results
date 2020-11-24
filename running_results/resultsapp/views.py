from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventsForm
from .helper import Helper
from .models import Distance, Event


def distance_detail_view(request, id):
    obj = get_object_or_404(Distance, id=id)
    obj.min = Helper.convert_from_seconds(obj.min)
    obj.max = Helper.convert_from_seconds(obj.max)
    context = {
        "object": obj
    }
    return render(request, "resultsapp/distance_detail.html", context)


def distances_list_view(request):
    queryset = Distance.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "resultsapp/distances_list.html", context)


def events_create_view(request):
    form = EventsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EventsForm()
    context = {
        'form': form
    }
    return render(request, "resultsapp/events_create.html", context)


def events_update_view(request, id=id):
    obj = get_object_or_404(Event, id=id)
    form = EventsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "resultsapp/events_create.html", context)


def events_for_year_list_view(request, year):
    queryset = Event.objects.filter(date__iregex=r"{}.*".format(year)).order_by('-date')
    queryset_years = Event.objects.all().order_by('-date')
    years = []
    for item in queryset_years:
        year = item.date.year
        if not year in years:
            years.append(year)
    context = {
        "object_list": queryset,
        "year_list": years,
    }
    return render(request, "resultsapp/events_for_year_list.html", context)


def events_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    context = {
        "object": obj
    }
    return render(request, "resultsapp/event_details.html", context)


def events_delete_view(request, id):
    obj = get_object_or_404(Event, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "resultsapp/events_delete.html", context)


def get_years_with_events_view(request):
    queryset = Event.objects.all().order_by('-date')
    years = []
    for item in queryset:
        year = item.date.year
        if not year in years:
            years.append(year)
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/events_year_filter.html", context)