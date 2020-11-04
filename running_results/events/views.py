from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventsForm
from .models import Event


def events_create_view(request):
    form = EventsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EventsForm()
    context = {
        'form': form
    }
    return render(request, "events/events_create.html", context)


def events_update_view(request, id=id):
    obj = get_object_or_404(Event, id=id)
    form = EventsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "events/events_create.html", context)


def events_list_view(request, year):
    #queryset = Event.objects.all().order_by('-date') # list of objects
    queryset = Event.objects.filter(date__iregex=r'2020.*').order_by('-date')
    context = {
        "object_list": queryset
    }
    return render(request, "events/events_list.html", context)


def events_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    context = {
        "object": obj
    }
    return render(request, "events/events_detail.html", context)


def events_delete_view(request, id):
    obj = get_object_or_404(Event, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "events/events_delete.html", context)


def get_years_with_events(request):
    queryset = Event.objects.all().order_by('-date')
    years = []
    for item in queryset:
        year = item.date.year
        if not year in years:
            years.append(year)
    context = {
        "year_list": years
    }
    return render(request, "events/year_filter.html", context)