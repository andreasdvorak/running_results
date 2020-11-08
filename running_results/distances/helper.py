from django.db.models import Max
from .models import Distances

import logging
import time

logger = logging.getLogger('consolefile')

class Helper():
    # not tested, output e.g 10:17:35
    def convert_from_seconds(self, seconds):
        ty_res = time.gmtime(seconds)
        result = time.strftime("%H:%M:%S",ty_res)
        return result


    def convert_to_seconds(self, time_str):
        try:
            h, m ,s = time_str.split(':')
            totalSeconds = int(h) * 3600 + int(m) * 60 + int(s)
            return totalSeconds
        except ValueError:
            logger.error("Wrong time:" + time_str)


    # get highest sort number
    def get_highest_sort(self):
        sort_max = Distances.objects.all().aggregate(Max('sort'))
        for key, value in sort_max.items():
            if value:
                max_sort = value
            else:
                max_sort = 0
        return max_sort