from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventsForm
from .helper import Helper
from .models import Distance, Event, Result
import logging

logger = logging.getLogger('console_file')


def annual_records_m_view(request, year):
    logger.debug('create annual record list male for year ' + str(year))
    distance_queryset = Distance.objects.all()
    records = []
    for distance in distance_queryset:
        distance_object = Distance.objects.get(name=distance)
        logger.debug('distance.id: ' + str(distance_object.id))
        result_queryset = Result.objects.filter(distance_id=distance_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug('member: ' + str(member))
            sex = Helper.get_sex_from_result_member(member)
            if sex == "m":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records.append(result_item)
                    logger.debug('added result_item: ' + str(result_item))
                    break
    years = Helper.get_years_with_events()
    context = {
        "result_object_list": records,
        "year_list": years,
    }
    return render(request, "resultsapp/annual_record_list_m.html", context)


def annual_records_w_view(request, year):
    logger.debug('create annual record list female for year ' + str(year))
    distance_queryset = Distance.objects.all()
    records = []
    for distance in distance_queryset:
        distance_object = Distance.objects.get(name=distance)
        logger.debug('distance.id: ' + str(distance_object.id))
        result_queryset = Result.objects.filter(distance_id=distance_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug('member: ' + str(member))
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records.append(result_item)
                    logger.debug('added result_item: ' + str(result_item))
                    break
    years = Helper.get_years_with_events()
    context = {
        "result_object_list": records,
        "year_list": years,
    }
    return render(request, "resultsapp/annual_record_list_w.html", context)


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
    years = Helper.get_years_with_events()
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


def get_years_with_annual_records_m_view(request):
    years = Helper.get_years_with_events()
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/annual_records_m_filter.html", context)


def get_years_with_annual_records_w_view(request):
    years = Helper.get_years_with_events()
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/annual_records_w_filter.html", context)


def get_years_with_events_view(request):
    years = Helper.get_years_with_events()
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
            sex = Helper.get_sex_from_result_member(member)
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
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                records.append(result_item)
                break
            logger.debug('result_item: ' + str(result_item))

    context = {
        "result_object_list": records,
    }
    return render(request, "resultsapp/record_list_w.html", context)


def statistics_view(request):
    logger.debug('show statistic')
    statistics = []
    event_count = Event.objects.all().count()
    statistics.append("Number of events: " + str(event_count))
    result_count = Result.objects.all().count()
    statistics.append("Number of results: " + str(result_count))
    context = {
        "object_list": statistics,
    }
    return render(request, "resultsapp/statistics.html", context)
