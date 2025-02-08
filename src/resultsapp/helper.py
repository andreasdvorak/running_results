"""Module to define helper functions"""

import datetime
import logging

from django.db.models import Max
from .models import DisciplineDistance, DisciplineTime, Event

logger = logging.getLogger('console_file')


class Helper():
    """Helper Class with helper functions

    Returns:
        _type_: _description_
    """
    @staticmethod
    def convert_from_seconds(seconds):
        """convert from seconds to hh:mm:ss

        Args:
            seconds (_type_): seconds to convert

        Returns:
            _type_: _description_
        """
        result = datetime.timedelta(seconds=seconds)
        return result

    @staticmethod
    def convert_to_seconds(time_str):
        """convert time string to seconds

        Args:
            time_str (_type_): hh:mm:ss

        Returns:
            int: seconds
        """
        try:
            h, m, s = time_str.split(':')
            total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
            return total_seconds
        except ValueError:
            logger.error("Wrong time: %s", time_str)

        return None

    @staticmethod
    def get_highest_discipline_distance_sort():
        """get highest sort number of distance disciplines

        Returns:
            _type_: _description_
        """
        max_sort = 0
        sort_max = DisciplineDistance.objects.all().aggregate(Max('sort'))
        for _, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort

    @staticmethod
    # get highest sort number
    def get_highest_discipline_time_sort():
        """get highest sort number of time discipline

        Returns:
            _type_: _description_
        """
        max_sort = 0
        sort_max = DisciplineTime.objects.all().aggregate(Max('sort'))
        for _, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort

    @staticmethod
    def get_sex_from_result_member(member):
        """get sec of member

        Args:
            member (_type_): lastname3, firstname3 m 2000

        Returns:
            string: sex of member
        """
        sex = str(member).split(" ")[2]
        return sex

    @staticmethod
    def get_years_with_events():
        """get years where at least one events exists

        Returns:
            list: years of events
        """
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
        """get year from an event

        Args:
            event (_type_): 2020-10-20 Frankfurt

        Returns:
            string: year
        """
        year = str(event).split("-")[0]
        return year
