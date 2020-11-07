import csv
import io
import logging
from django import forms
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from io import StringIO

from .models import Distances

# Get an instance of a logger
logger = logging.getLogger(__name__)

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class DistancesAdmin(admin.ModelAdmin):
    list_display = ('sort', 'name', 'min', 'max', 'category')

    # begin csv import
    change_list_template = "distances/distances_changelist.html"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        logger.info('---------------------------Hello')
        if request.method == "POST":
            #csv_file = request.FILES["csv_file"]
            with io.TextIOWrapper(request.FILES["csv_file"], newline='\n') as text_file:
            #with io.TextIOWrapper(request.FILES["csv_file"].chunks(), encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')                
            #content = StringIO(request.FILES["csv_file"].read().decode('latin-1'))
            #reader = csv.reader(content, delimiter=';')
            # todo get highest sort number
            sort = 1
            for row in reader:
                logger.info('row:' + str(row))
                #min = int(row[0])
                min = 1
                #max = int(row[1])
                max = 2
                name = row[2]
                #category = row[3]
                category = 't'
                #Distances.objects.create(
                #    sort = sort + 1,
                #    min = min,
                #    max = max,
                #    name = name,
                #    category = category
                #    )
                
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "distances/csv_form.html", payload
        )
        # end csv import

admin.site.register(Distances, DistancesAdmin)