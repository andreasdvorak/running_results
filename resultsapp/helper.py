from django.db.models import Max
from .models import DisciplineDistance, DisciplineTime, Event

import datetime
import logging

logger = logging.getLogger('console_file')


class Helper():
    @staticmethod
    def convert_from_seconds(seconds):
        result = datetime.timedelta(seconds=seconds)
        return result

    @staticmethod
    def convert_to_seconds(time_str):
        try:
            h, m, s = time_str.split(':')
            total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
            return total_seconds
        except ValueError:
            logger.error("Wrong time:" + time_str)

    @staticmethod
    # get highest sort number
    def get_highest_discipline_distance_sort():
        max_sort = 0
        sort_max = DisciplineDistance.objects.all().aggregate(Max('sort'))
        for key, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort

    @staticmethod
    # get highest sort number
    def get_highest_discipline_time_sort():
        max_sort = 0
        sort_max = DisciplineTime.objects.all().aggregate(Max('sort'))
        for key, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort

    @staticmethod
    # member = "lastname3, firstname3 m 2000"
    def get_sex_from_result_member(member):
        sex = str(member).split(" ")[2]
        return sex

    @staticmethod
    def get_years_with_events():
        queryset = Event.objects.all().order_by('-date')
        years = []
        for item in queryset:
            year = item.date.year
            if year not in years:
                years.append(year)
        return years

    @staticmethod
    # event = "2020-10-20 Frankfurt"
    def get_year_from_result_event(event):
        year = str(event).split("-")[0]
        return year
