import csv
import io
import logging
from django import forms
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from .models import Distances
from .helper import Helper

# Get an instance of a logger
logger = logging.getLogger('consolefile')

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class DistancesAdmin(admin.ModelAdmin):
    list_display = ('sort', 'name', 'min', 'max', 'category')
    delete_display = ('sort', 'name', 'min', 'max', 'category')


    # begin csv import
    change_list_template = "distances/distances_changelist.html"
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
                    
                    sort_max = Helper.get_highest_sort()
                    logger.info('sort_max:' + str(sort_max))
                    sort = sort_max +1
                    logger.info('values to import: ' + str(sort) + ', ' + str(min) + ', ' + str(max) + ', ' + name + ', ' + category)
                    Distances.objects.create(
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
            request, "distances/csv_form.html", payload
        )
        # end csv import


admin.site.register(Distances, DistancesAdmin)