"""Module for admin tasks"""
import csv
import io
import logging
from django import forms
from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import path
from django.utils.html import format_html
from .actions import export_member_csv, export_results_csv
from .helper import Helper
from .models import AgeGroup, Club, Event, DisciplineDistance, DisciplineTime, Member, ResultDistance, ResultTime

# Get an instance of a logger
logger = logging.getLogger('console_file')


class CsvImportForm(forms.Form):
    """Form to import a csv file

    Args:
        forms (_type_): _description_
    """
    csv_file = forms.FileField()


class AgeGroupAdmin(admin.ModelAdmin):
    """Administration of age groups

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ('age', 'age_group_m', 'age_group_w')

    # begin csv import
    change_list_template = "resultsapp/age_groups_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    # TODO: try with pandas
    def import_csv(self, request):
        """Import csv file with age groups

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')
                for row in reader:
                    logger.debug("row in csv file: %s", row)
                    age = row[0]
                    age_group_m = row[1]
                    age_group_w = row[2]
                    logger.debug("values to import: %s, %s, %s", age, age_group_m, age_group_w)
                    AgeGroup.objects.create(
                        age=age,
                        age_group_m=age_group_m,
                        age_group_w=age_group_w,
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import


class ClubAdmin(admin.ModelAdmin):
    """Class for adminstration of the club details

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ('name', 'email', 'info', 'allow_public_record')

    # only one instance allowed
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class DisciplineDistanceAdmin(admin.ModelAdmin):
    """Administration of distance disciplines

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ('sort', 'name', 'min', 'max')
    delete_display = ('sort', 'name', 'min', 'max')

    # begin csv import
    change_list_template = "resultsapp/disciplines_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    # TODO: try with pandas
    def import_csv(self, request):
        """Import csv file with distance disciplines

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')
                for row in reader:
                    logger.debug("row in csv file: %s", row)
                    min_value = row[0]
                    max_value = row[1]
                    name = row[2]
                    sort_max = Helper.get_highest_discipline_distance_sort()
                    logger.debug("sort_max: %s", sort_max)
                    sort = sort_max + 1
                    logger.debug("values to import: %s, %s, %s, %s",
                                 sort, min_value, max_value, name)
                    DisciplineDistance.objects.create(
                        sort=sort,
                        min=min_value,
                        max=max_value,
                        name=name
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "resultsapp/csv_form.html", payload
        )
        # end csv import


class DisciplineTimeAdmin(admin.ModelAdmin):
    """Administration of time disciplines

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ('sort', 'name', 'min', 'max')
    delete_display = ('sort', 'name', 'min', 'max')

    # begin csv import
    change_list_template = "resultsapp/disciplines_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    # TODO: try with pandas
    def import_csv(self, request):
        """Import csv file

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')
                for row in reader:
                    logger.debug("row in csv file: %s", row)
                    min_value = row[0]
                    max_value = row[1]
                    name = row[2]
                    sort_max = Helper.get_highest_discipline_time_sort()
                    logger.debug("sort_max: %s", sort_max)
                    sort = sort_max + 1
                    logger.debug("values to import: %s, %s, %s, %s", sort, min_value, max_value, name)
                    DisciplineTime.objects.create(
                        sort=sort,
                        min=min_value,
                        max=max_value,
                        name=name
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
    """Administration of events

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    list_display = ('date', 'location', 'custom_url', 'note')
    list_filter = ('date', 'location')

    # begin csv import
    change_list_template = "resultsapp/event_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    # TODO: try pandas
    def import_csv(self, request):
        """Import csv file

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')
                for row in reader:
                    logger.debug("row in csv file: %s", row)
                    logger.debug("columns: %s", len(row))
                    date = row[0]
                    location = row[1]
                    website = row[2]
                    note = row[3]
                    logger.debug("values to import: %s, %s, %s, %s", date, location, website, note)
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
        """_summary_

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        return format_html('<a href="{0}" >{0}</a>&nbsp;', obj.website)

    custom_url.short_description = 'Website'
    custom_url.admin_order_field = 'website'


class MemberAdmin(admin.ModelAdmin):
    """Adminstration of member

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
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
        """Import csv file

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        if request.method == "POST":
            # convert from binary to text
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')
                for row in reader:
                    logger.debug("row in csv file: %s", row)
                    firstname = row[0]
                    lastname = row[1]
                    sex = row[2]
                    year_of_birth = row[3]
                    logger.debug("values to import: %s, %s, %s, %s",
                                 firstname, lastname, sex, year_of_birth)
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


class ResultDistanceAdmin(admin.ModelAdmin):
    """Administration of distance results

    Args:
        admin (_type_): _description_

    Returns:
        _type_: _description_
    """
    # what files are shown in form
    fields = ['result_value', 'discipline_id', 'event_id', 'member_id']
    # show result data
    list_display = ('time_seconds', 'discipline_id', 'age_group', 'member_id', 'event_id')
    # show filer
    list_filter = ('age_group', 'discipline_id', 'member_id', 'event_id')

    actions = [export_results_csv]

    def time_seconds(self, obj):
        """define the format of result_value, otherwise seconds are missing

        Args:
            obj (_type_): _description_

        Returns:
            _type_: _description_
        """
        return obj.result_value.strftime("%H:%M:%S")

    time_seconds.short_description = 'Time'

    def save_model(self, request, obj, form, change):
        # get year_of_birth
        logger.debug("save_model member_id: %s", form.cleaned_data['member_id'])
        member_data = str(form.cleaned_data['member_id']).split(" ")
        sex = member_data[2]
        logger.debug("save_model sex: %s", sex)
        year_of_birth = member_data[3]
        logger.debug("save_model year_of_birth: %s", year_of_birth)
        # get date
        logger.debug("save_model event_id: %s", form.cleaned_data['event_id'])
        event_data = str(form.cleaned_data['event_id']).split(" ")
        date = event_data[0]
        year_of_event = date.split("-")[0]
        logger.debug("save_model year_of_event: %s", year_of_event)
        age = int(year_of_event) - int(year_of_birth)
        logger.debug("save_model age: %s", age)
        # get the age_group
        obj_age_group = get_object_or_404(AgeGroup, age=age)
        age_group_id = obj_age_group.age
        logger.debug("save_model age_group_id: %s", age_group_id)
        if sex == 'm':
            age_group = obj_age_group.age_group_m
        else:
            age_group = obj_age_group.age_group_w
        obj.age_group = age_group
        # finally save the object in db
        super().save_model(request, obj, form, change)


class ResultTimeAdmin(admin.ModelAdmin):
    """Administration of time results

    Args:
        admin (_type_): _description_
    """
    # what files are shown in form
    fields = ['result_value', 'discipline_id', 'event_id', 'member_id']
    # show result data
    list_display = ('result_value', 'discipline_id', 'age_group', 'member_id', 'event_id')
    # show filer
    list_filter = ('age_group', 'discipline_id', 'member_id', 'event_id')

    actions = [export_results_csv]

    def save_model(self, request, obj, form, change):
        # get year_of_birth
        logger.debug("save_model member_id: %s", form.cleaned_data['member_id'])
        member_data = str(form.cleaned_data['member_id']).split(" ")
        sex = member_data[2]
        logger.debug("save_model sex: %s", sex)
        year_of_birth = member_data[3]
        logger.debug("save_model year_of_birth: %s", year_of_birth)
        # get date
        logger.debug("save_model event_id: %s", form.cleaned_data['event_id'])
        event_data = str(form.cleaned_data['event_id']).split(" ")
        date = event_data[0]
        year_of_event = date.split("-")[0]
        logger.debug("save_model year_of_event: %s", year_of_event)
        age = int(year_of_event) - int(year_of_birth)
        logger.debug("save_model age: %s", age)
        # get the age_group
        obj_age_group = get_object_or_404(AgeGroup, age=age)
        age_group_id = obj_age_group.age
        logger.debug("save_model age_group_id: %s", age_group_id)
        if sex == 'm':
            age_group = obj_age_group.age_group_m
        else:
            age_group = obj_age_group.age_group_w
        obj.age_group = age_group
        # finally save the object in db
        super().save_model(request, obj, form, change)


admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(DisciplineDistance, DisciplineDistanceAdmin)
admin.site.register(DisciplineTime, DisciplineTimeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(ResultDistance, ResultDistanceAdmin)
admin.site.register(ResultTime, ResultTimeAdmin)
