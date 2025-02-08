"""Module rendering html files"""

import logging

from django.shortcuts import render, get_object_or_404
from .forms import EventsForm
from .helper import Helper
from .models import Club, DisciplineDistance, DisciplineTime, Event, ResultDistance, ResultTime

logger = logging.getLogger('console_file')


def annual_records_m_view(request, year):
    """render html file to show annual records male for a year

    Args:
        request (_type_): _description_
        year (_type_): year to show the records

    Returns:
        _type_: _description_
    """
    logger.debug("create annual record list male for year %s", year)
    discipline_distance_queryset = DisciplineDistance.objects.all()
    records_distance = []
    for discipline in discipline_distance_queryset:
        discipline_object = DisciplineDistance.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultDistance.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "m":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records_distance.append(result_item)
                    logger.debug("added result_item: %s", result_item)
                    break
    discipline_time_queryset = DisciplineTime.objects.all()
    records_time = []
    for discipline in discipline_time_queryset:
        discipline_object = DisciplineTime.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultTime.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "m":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records_time.append(result_item)
                    logger.debug("added result_item: %s", result_item)
                    break
    years = Helper.get_years_with_events()
    context = {
        "result_distance_object_list": records_distance,
        "result_time_object_list": records_time,
        "year_list": years,
        "year": year
    }
    return render(request, "resultsapp/annual_record_list_m.html", context)


def annual_records_w_view(request, year):
    """render html file to show annual records female for a year

    Args:
        request (_type_): _description_
        year (_type_): year to show the records

    Returns:
        _type_: _description_
    """
    logger.debug("create annual record list male for year %s", year)
    discipline_distance_queryset = DisciplineDistance.objects.all()
    records_distance = []
    for discipline in discipline_distance_queryset:
        discipline_object = DisciplineDistance.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultDistance.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records_distance.append(result_item)
                    logger.debug("added result_item: %s", result_item)
                    break
    discipline_time_queryset = DisciplineTime.objects.all()
    records_time = []
    for discipline in discipline_time_queryset:
        discipline_object = DisciplineTime.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultTime.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                event = result_item.event_id
                if str(year) == Helper.get_year_from_result_event(event):
                    records_time.append(result_item)
                    logger.debug("added result_item: %s", result_item)
                    break
    years = Helper.get_years_with_events()
    context = {
        "result_distance_object_list": records_distance,
        "result_time_object_list": records_time,
        "year_list": years,
        "year": year
    }
    return render(request, "resultsapp/annual_record_list_w.html", context)


def about_view(request, *args, **kwargs):
    """render html file about the software

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "about.html", {})


def club_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    obj = Club.objects.all()
    context = {
        "object": obj
    }
    return render(request, "resultsapp/club_view.html", context)


def discipline_detail_view(request, id):
    """render html file to show the details of one discipline

    Returns:
        _type_: _description_
    """
    obj = get_object_or_404(DisciplineDistance, id=id)
    obj.min = Helper.convert_from_seconds(obj.min)
    obj.max = Helper.convert_from_seconds(obj.max)
    context = {
        "object": obj
    }
    return render(request, "resultsapp/discipline_detail.html", context)


def discipline_list_view(request):
    """render html file to list the disclines

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    queryset_distance = DisciplineDistance.objects.all()
    queryset_time = DisciplineTime.objects.all()
    context = {
        "queryset_distance": queryset_distance,
        "queryset_time": queryset_time
    }
    return render(request, "resultsapp/discipline_list.html", context)


def event_create_view(request):
    """render html file to create an event

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    form = EventsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EventsForm()
    context = {
        'form': form
    }
    return render(request, "resultsapp/event_create.html", context)


def event_for_year_list_view(request, year):
    """render html for the view of events of one year

    Args:
        request (_type_): _description_
        year (_type_): year to show the events for

    Returns:
        _type_: _description_
    """
    queryset = Event.objects.filter(date__iregex=r"{}.*".format(year)).order_by('-date')
    years = Helper.get_years_with_events()
    context = {
        "object_list": queryset,
        "year_list": years,
    }
    return render(request, "resultsapp/event_for_year_list.html", context)


def event_detail_view(request, id):
    """render html for event details

    Args:
        request (_type_): _description_
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    obj = get_object_or_404(Event, id=id)
    context = {
        "object": obj
    }
    return render(request, "resultsapp/event_details.html", context)


def home_view(request, *args, **kwargs):
    """render home.html

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def record_list_m_view(request):
    """create the record list for male

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug('create record list male')
    discipline_distance_queryset = DisciplineDistance.objects.all()
    records_distance = []
    for discipline in discipline_distance_queryset:
        discipline_object = DisciplineDistance.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultDistance.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "m":
                records_distance.append(result_item)
                break
            logger.debug("result_item: %s", result_item)
    discipline_time_queryset = DisciplineTime.objects.all()
    records_time = []
    for discipline in discipline_time_queryset:
        discipline_object = DisciplineTime.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultTime.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "m":
                records_time.append(result_item)
                break
            logger.debug("result_item: %s", result_item)

    context = {
        "result_distance_object_list": records_distance,
        "result_time_object_list": records_time
    }
    return render(request, "resultsapp/record_list_m.html", context)


def record_list_w_view(request):
    """create record list for female

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug('create record list female')
    discipline_distance_queryset = DisciplineDistance.objects.all()
    records_distance = []
    for discipline in discipline_distance_queryset:
        discipline_object = DisciplineDistance.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultDistance.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                records_distance.append(result_item)
                break
            logger.debug("result_item: %s", result_item)
    discipline_time_queryset = DisciplineTime.objects.all()
    records_time = []
    for discipline in discipline_time_queryset:
        discipline_object = DisciplineTime.objects.get(name=discipline)
        logger.debug("discipline.id: %s", discipline_object.id)
        result_queryset = ResultTime.objects.filter(
            discipline_id=discipline_object.id).order_by('result_value')
        for result_item in result_queryset:
            member = result_item.member_id
            logger.debug("member: %s", member)
            sex = Helper.get_sex_from_result_member(member)
            if sex == "w":
                records_time.append(result_item)
                break
            logger.debug("result_item: %s", result_item)

    context = {
        "result_distance_object_list": records_distance,
        "result_time_object_list": records_time
    }
    return render(request, "resultsapp/record_list_w.html", context)


def statistics_view(request):
    """generate view for statistics

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    logger.debug("show statistic")
    statistics = []

    event_count = Event.objects.all().count()
    statistics.append("Number of events: " + str(event_count))

    years = Helper.get_years_with_events()
    for year in years:
        event_count = Event.objects.filter(date__iregex=r"{}.*".format(year)).count()
        statistics.append("Number of events in " + str(year) + ": " + str(event_count))

    result_count_distance = ResultDistance.objects.all().count()
    result_count_time = ResultTime.objects.all().count()
    result_count = int(result_count_distance) + int(result_count_time)
    statistics.append("Number of results: " + str(result_count))

    result_distance_queryset = ResultDistance.objects.all()
    result_time_queryset = ResultTime.objects.all()
    for year in years:
        logger.debug("year: %s", year)
        result_counter = 0
        for result in result_distance_queryset:
            logger.debug(str(result.event_id))
            if str(year) == Helper.get_year_from_result_event(result.event_id):
                result_counter = result_counter + 1
        for result in result_time_queryset:
            logger.debug(str(result.event_id))
            if str(year) == Helper.get_year_from_result_event(result.event_id):
                result_counter = result_counter + 1
        statistics.append(f"Number of results in {year}, {result_counter}")

    context = {
        "object_list": statistics,
    }
    return render(request, "resultsapp/statistics.html", context)


def years_with_annual_records_m_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    years = Helper.get_years_with_events()
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/annual_records_m_filter.html", context)


def years_with_annual_records_w_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    years = Helper.get_years_with_events()
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/annual_records_w_filter.html", context)


def years_with_events_view(request):
    """show the years with events

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    years = Helper.get_years_with_events()
    context = {
        "year_list": years
    }
    return render(request, "resultsapp/event_year_filter.html", context)
