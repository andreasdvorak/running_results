import csv
import io
import logging
from django import forms
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from .models import Agegroup

logger = logging.getLogger('consolefile')

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class AgegroupAdmin(admin.ModelAdmin):
    list_display = ('age', 'agegroupm', 'agegroupw')

    # begin csv import
    change_list_template = "agegroups/agegroups_changelist.html"
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
            request, "distances/csv_form.html", payload
        )
        # end csv import


admin.site.register(Agegroup, AgegroupAdmin)