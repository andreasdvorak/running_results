from django import forms
from django.contrib import admin
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import path
from django.utils.html import format_html
from .helper import Helper
from .models import Agegroup, Event, Distance, Member, Result
import csv
import io
import logging


# Get an instance of a logger
logger = logging.getLogger('consolefile')


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class AgegroupAdmin(admin.ModelAdmin):
    list_display = ('age', 'agegroupm', 'agegroupw')

    # begin csv import
    change_list_template = "results/agegroups_changelist.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')                
                for row in reader:
                    logger.info('row in csv file:' + str(row))
                    age = row[0]
                    agegroupm = row[1]
                    agegroupw = row[2]
                    logger.info('values to import: ' + str(age) + ', ' + str(agegroupm) + ', ' + str(agegroupw))
                    Agegroup.objects.create(
                        age = age,
                        agegroupm = agegroupm,
                        agegroupw = agegroupw,
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "results/csv_form.html", payload
        )
        # end csv import


class DistanceAdmin(admin.ModelAdmin):
    list_display = ('sort', 'name', 'min', 'max', 'category')
    delete_display = ('sort', 'name', 'min', 'max', 'category')


    # begin csv import
    change_list_template = "results/distances_changelist.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls


    def import_csv(self, request):
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')                
                for row in reader:
                    logger.info('row in csv file:' + str(row))
                    if row[3] == 'distance':
                        category = 'd'
                        min = Helper.convert_to_seconds(row[0])
                        max = Helper.convert_to_seconds(row[1])
                    else:
                        category = 't'
                        min = row[0]
                        max = row[1]
                    name = row[2]
                    
                    sort_max = Helper.get_highest_distance_sort()
                    logger.info('sort_max:' + str(sort_max))
                    sort = sort_max +1
                    logger.info('values to import: ' + str(sort) + ', ' + str(min) + ', ' + str(max) + ', ' + name + ', ' + category)
                    Distance.objects.create(
                        sort = sort,
                        min = min,
                        max = max,
                        name = name,
                        category = category
                    )
                
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "results/csv_form.html", payload
        )
        # end csv import


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'custom_url', 'note')

    def custom_url(self, obj):
        return format_html(
        '<a href="{0}" >{0}</a>&nbsp;',
            obj.website
        )
    custom_url.short_description = 'Website'
    custom_url.admin_order_field = 'website'


class MemberAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'sex', 'year_of_birth')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_value','get_distance_name')

    def get_distance_name(self, obj):
        obj_distance = get_object_or_404(Distance, id=obj.id)
        name = obj_distance.name
        logger.info('name:' + name)
        return name
    get_distance_name.short_description = 'Distance Name'


admin.site.register(Agegroup, AgegroupAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Result, ResultAdmin)