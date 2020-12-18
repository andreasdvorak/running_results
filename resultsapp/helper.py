from django.db.models import Max
from .models import Distance

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
            totalseconds = int(h) * 3600 + int(m) * 60 + int(s)
            return totalseconds
        except ValueError:
            logger.error("Wrong time:" + time_str)

    @staticmethod
    # get highest sort number
    def get_highest_distance_sort():
        max_sort = 0
        sort_max = Distance.objects.all().aggregate(Max('sort'))
        for key, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort
