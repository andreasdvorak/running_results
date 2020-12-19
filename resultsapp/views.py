from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventsForm
from .helper import Helper
from .models import Distance, Event, Result
import logging

logger = logging.getLogger('console_file')


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


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
        if year not in years:
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
        if year not in years:
            years.append(year)
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/events_year_filter.html", context)


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def record_list_m_view(request):
    logger.debug('create record list male')
    distance_queryset = Distance.objects.all()
    records = []
    for distance in distance_queryset:
        distance_object = Distance.objects.get(name=distance)
        logger.debug('distance.id: ' + str(distance_object.id))
        result_queryset = Result.objects.filter(distance_id=distance_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug('member: ' + str(member))
            sex = str(member).split(" ")[2]
            if sex == "m":
                records.append(result_item)
                break
            logger.debug('result_item: ' + str(result_item))

    context = {
        "result_object_list": records,
    }
    return render(request, "resultsapp/record_list_m.html", context)


def record_list_w_view(request):
    logger.debug('create record list female')
    distance_queryset = Distance.objects.all()
    records = []
    for distance in distance_queryset:
        distance_object = Distance.objects.get(name=distance)
        logger.debug('distance.id: ' + str(distance_object.id))
        result_queryset = Result.objects.filter(distance_id=distance_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug('member: ' + str(member))
            sex = str(member).split(" ")[2]
            if sex == "w":
                records.append(result_item)
                break
            logger.debug('result_item: ' + str(result_item))

    context = {
        "result_object_list": records,
    }
    return render(request, "resultsapp/record_list_w.html", context)
