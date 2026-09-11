"""Module rendering html files"""

import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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
        "year_choices": _annual_record_year_choices("m", year),
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
        "year_choices": _annual_record_year_choices("w", year),
        "year": year
    }
    return render(request, "resultsapp/annual_record_list_w.html", context)


def _annual_record_year_choices(sex, selected_year=None):
    """Build year options for annual record views."""
    return [
        {"url": reverse(
            f"resultsapp:annual-records-{sex}-for-year-list",
            kwargs={"year": year}),
         "value": year,
         "selected_attribute": " selected" if year == selected_year else ""}
        for year in Helper.get_years_with_events()
    ]


def about_view(request, *_args, **_kwargs):
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


def discipline_detail_view(request, discipline_id):
    """render html file to show the details of one discipline

    Returns:
        _type_: _description_
    """
    obj = get_object_or_404(DisciplineDistance, id=discipline_id)
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
    queryset = Event.objects.filter(date__iregex=fr"{year}.*").order_by('-date')
    years = Helper.get_years_with_events()
    year_choices = [
        {"url": reverse("resultsapp:event-for-year-list",
                         kwargs={"year": available_year}),
         "value": available_year,
         "selected_attribute": " selected" if available_year == year else ""}
        for available_year in years
    ]
    context = {
        "object_list": queryset,
        "year_choices": year_choices,
    }
    return render(request, "resultsapp/event_for_year_list.html", context)


def event_detail_view(request, event_id):
    """render html for event details

    Args:
        request (_type_): _description_
        event_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    obj = get_object_or_404(Event, id=event_id)
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


def annual_results_m_view(request, year):
    """Show all male results for one year."""
    context = _annual_results_context(request, year, "m")
    return render(request, "resultsapp/annual_results_m.html", context)


def annual_results_w_view(request, year):
    """Show all female results for one year."""
    context = _annual_results_context(request, year, "w")
    return render(request, "resultsapp/annual_results_w.html", context)


def _annual_results_context(request, year, sex):
    """Build the context for the annual result views."""
    result_distance_queryset = ResultDistance.objects.filter(
        event_id__date__year=year, member_id__sex=sex).order_by(
            "event_id__date", "discipline_id", "result_value")
    result_time_queryset = ResultTime.objects.filter(
        event_id__date__year=year, member_id__sex=sex).order_by(
            "event_id__date", "discipline_id", "result_value")

    discipline_choices = [
        {"value": f"distance:{discipline.id}",
         "label": f"Distance: {discipline.name}"}
        for discipline in DisciplineDistance.objects.all()
    ]
    discipline_choices.extend(
        {"value": f"time:{discipline.id}",
         "label": f"Time: {discipline.name}"}
        for discipline in DisciplineTime.objects.all()
    )
    selected_discipline = request.GET.get("discipline", "")
    discipline_type, separator, discipline_id = selected_discipline.partition(":")
    selected_discipline_type = ""
    if separator and discipline_id.isdigit():
        if discipline_type == "distance":
            selected_discipline_type = "distance"
            result_distance_queryset = result_distance_queryset.filter(
                discipline_id=discipline_id)
            result_time_queryset = result_time_queryset.none()
        elif discipline_type == "time":
            selected_discipline_type = "time"
            result_distance_queryset = result_distance_queryset.none()
            result_time_queryset = result_time_queryset.filter(
                discipline_id=discipline_id)
        else:
            selected_discipline = ""
    else:
        selected_discipline = ""

    for discipline in discipline_choices:
        discipline["selected"] = discipline["value"] == selected_discipline

    year_choices = [
        {"value": available_year,
         "url": reverse(
             f"resultsapp:annual-results-{sex}-for-year-list",
             kwargs={"year": available_year}),
         "selected_attribute": " selected" if available_year == year else ""}
        for available_year in Helper.get_years_with_events()
    ]

    return {
        "result_distance_object_list": result_distance_queryset,
        "result_time_object_list": result_time_queryset,
        "year_list": [choice["value"] for choice in year_choices],
        "year_choices": year_choices,
        "discipline_choices": discipline_choices,
        "show_distance_results": selected_discipline_type == "distance",
        "show_time_results": selected_discipline_type == "time",
        "discipline_selected": bool(selected_discipline_type),
        "year": year,
    }


def _count_results_for_year(year, result_querysets):
    """Return total, male, and female result counts for a year."""
    result_counter = 0
    male_result_counter = 0
    female_result_counter = 0
    for result_queryset in result_querysets:
        for result in result_queryset:
            logger.debug(str(result.event_id))
            if str(year) == Helper.get_year_from_result_event(result.event_id):
                result_counter += 1
                sex = Helper.get_sex_from_result_member(result.member_id)
                if sex == "m":
                    male_result_counter += 1
                elif sex == "w":
                    female_result_counter += 1
    return result_counter, male_result_counter, female_result_counter


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
        event_count = Event.objects.filter(date__iregex=fr"{year}.*").count()
        statistics.append("Number of events in " + str(year) + ": " + str(event_count))

    result_count_distance = ResultDistance.objects.all().count()
    result_count_time = ResultTime.objects.all().count()
    result_count = int(result_count_distance) + int(result_count_time)
    statistics.append("Number of results: " + str(result_count))

    result_distance_queryset = ResultDistance.objects.all()
    result_time_queryset = ResultTime.objects.all()
    for year in years:
        logger.debug("year: %s", year)
        result_counter, male_result_counter, female_result_counter = (
            _count_results_for_year(
                year, (result_distance_queryset, result_time_queryset)))
        statistics.append(f"Number of results in {year}: {result_counter}")
        statistics.append(
            f"Number of results male in {year}: {male_result_counter}")
        statistics.append(
            f"Number of results female in {year}: {female_result_counter}")

    context = {
        "object_list": statistics,
    }
    return render(request, "resultsapp/statistics.html", context)


def years_with_annual_results_m_view(request):
    """Show years with results for male participants."""
    years = Helper.get_years_with_events()
    if years:
        return redirect("resultsapp:annual-results-m-for-year-list", year=years[0])
    return render(request, "resultsapp/annual_results_m_filter.html", {"year_list": []})


def years_with_annual_results_w_view(request):
    """Show years with results for female participants."""
    years = Helper.get_years_with_events()
    if years:
        return redirect("resultsapp:annual-results-w-for-year-list", year=years[0])
    return render(request, "resultsapp/annual_results_w_filter.html", {"year_list": []})


def years_with_annual_records_m_view(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    years = Helper.get_years_with_events()
    context = {
        "year_list": years,
        "year_choices": _annual_record_year_choices("m")
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
        "year_list": years,
        "year_choices": _annual_record_year_choices("w")
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
    if years:
        return redirect("resultsapp:event-for-year-list", year=years[0])
    return render(request, "resultsapp/event_for_year_list.html", {
        "object_list": [],
        "year_choices": [],
    })
