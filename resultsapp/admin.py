from django import forms
from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import path
from django.utils.html import format_html
from .actions import export_member_csv, export_results_csv
from .helper import Helper
from .models import Agegroup, Event, Distance, Member, Result
import csv
import io
import logging


# Get an instance of a logger
logger = logging.getLogger('console_file')


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class AgegroupAdmin(admin.ModelAdmin):
    list_display = ('age', 'agegroup_m', 'agegroup_w')

    # begin csv import
    change_list_template = "resultsapp/agegroups_changelist.html"

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
                    logger.debug('row in csv file:' + str(row))
                    age = row[0]
                    agegroup_m = row[1]
                    agegroup_w = row[2]
                    logger.debug('values to import: ' + str(age) + ', ' + str(agegroup_m) + ', ' + str(agegroup_w))
                    Agegroup.objects.create(
                        age=age,
                        agegroup_m=agegroup_m,
                        agegroup_w=agegroup_w,
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import


class DistanceAdmin(admin.ModelAdmin):
    list_display = ('sort', 'name', 'min', 'max', 'category')
    delete_display = ('sort', 'name', 'min', 'max', 'category')

    # begin csv import
    change_list_template = "resultsapp/distances_changelist.html"

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
                    logger.debug('row in csv file:' + str(row))
                    if row[3] == 'distance':
                        category = 'd'
                        min_value = Helper.convert_to_seconds(row[0])
                        max_value = Helper.convert_to_seconds(row[1])
                    else:
                        category = 't'
                        min_value = row[0]
                        max_value = row[1]
                    name = row[2]

                    sort_max = Helper.get_highest_distance_sort()
                    logger.debug('sort_max:' + str(sort_max))
                    sort = sort_max + 1
                    logger.debug('values to import: ' + str(sort) + ', ' + str(min_value) + ', ' + str(max_value)
                                 + ', ' + name + ', ' + category)
                    Distance.objects.create(
                        sort=sort,
                        min=min_value,
                        max=max_value,
                        name=name,
                        category=category
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import


class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'custom_url', 'note')
    list_filter = ('date', 'location')

    # begin csv import
    change_list_template = "resultsapp/events_changelist.html"

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
                    logger.debug('row in csv file:' + str(row))
                    logger.debug('columns:' + str(len(row)))
                    date = row[0]
                    location = row[1]
                    website = row[2]
                    note = row[3]
                    logger.debug('values to import: ' + str(date) + ', ' + str(location) + ', ' + str(website) + ', '
                                 + str(note))
                    Event.objects.create(
                        date=date,
                        location=location,
                        website=website,
                        note=note
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import

    def custom_url(self, obj):
        return format_html('<a href="{0}" >{0}</a>&nbsp;', obj.website)
    custom_url.short_description = 'Website'
    custom_url.admin_order_field = 'website'


class MemberAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'sex', 'year_of_birth')
    list_filter = ('lastname', 'firstname', 'sex', 'year_of_birth')
    search_fields = ("lastname__startswith", "firstname__startswith")

    actions = [export_member_csv]

    # begin csv import
    change_list_template = "resultsapp/member_changelist.html"

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
                    logger.debug('row in csv file:' + str(row))
                    firstname = row[0]
                    lastname = row[1]
                    sex = row[2]
                    year_of_birth = row[3]
                    logger.debug('values to import: ' + str(firstname) + ', ' + str(lastname) + ', ' + str(sex) + ', '
                                 + str(year_of_birth))
                    Member.objects.create(
                        firstname=firstname,
                        lastname=lastname,
                        sex=sex,
                        year_of_birth=year_of_birth
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import


class ResultAdmin(admin.ModelAdmin):
    # what files are shown in form
    fields = ['result_value', 'distance_id', 'event_id', 'member_id']
    # show result data
    list_display = ('time_seconds', 'distance_id', 'agegroup', 'member_id', 'event_id')
    # show filer
    list_filter = ('agegroup', 'distance_id', 'member_id', 'event_id')

    actions = [export_results_csv]

    # define the format of result_value, otherwise seconds are missing
    def time_seconds(self, obj):
        return obj.result_value.strftime("%H:%M:%S")
    time_seconds.short_description = 'Time'

    def save_model(self, request, obj, form, change):
        # get year_of_birth
        logger.debug("save_model member_id: " + str(form.cleaned_data['member_id']))
        member_data = str(form.cleaned_data['member_id']).split(" ")
        sex = member_data[2]
        logger.debug("save_model sex: " + str(sex))
        year_of_birth = member_data[3]
        logger.debug("save_model year_of_birth: " + str(year_of_birth))
        # get date
        logger.debug("save_model event_id: " + str(form.cleaned_data['event_id']))
        event_data = str(form.cleaned_data['event_id']).split(" ")
        date = event_data[0]
        year_of_event = date.split("-")[0]
        logger.debug("save_model year_of_event: " + str(year_of_event))
        age = int(year_of_event) - int(year_of_birth)
        logger.debug("save_model age: " + str(age))
        # get the agegroup
        obj_agegroup = get_object_or_404(Agegroup, age=age)
        agegroup_id = obj_agegroup.age
        logger.debug("save_model agegroup_id: " + str(agegroup_id))
        if sex == 'm':
            agegroup = obj_agegroup.agegroup_m
        else:
            agegroup = obj_agegroup.agegroup_w
        obj.agegroup = agegroup
        # finally save the object in db
        super().save_model(request, obj, form, change)


admin.site.register(Agegroup, AgegroupAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Result, ResultAdmin)
