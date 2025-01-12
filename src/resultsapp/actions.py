import csv
import logging
from django.http import HttpResponse
from django.utils.encoding import smart_str

logger = logging.getLogger('console_file')


def export_member_csv(modeladmin, request, queryset):
    logger.debug('export member to csv')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_export.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write('\ufeff'.encode('utf8'))
    writer.writerow([
        # smart_str("ID"),
        smart_str("Lastname"),
        smart_str("Firstname"),
        smart_str("Sex"),
        smart_str("Year of birth"),
    ])
    for obj in queryset:
        writer.writerow([
            # smart_str(obj.pk),
            smart_str(obj.lastname),
            smart_str(obj.firstname),
            smart_str(obj.sex),
            smart_str(obj.year_of_birth),
        ])
    return response


export_member_csv.short_description = "Export Member CSV"


def export_results_csv(modeladmin, request, queryset):
    logger.debug('export result to csv')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results_export.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        # smart_str(u"ID"),
        smart_str("Result_Value"),
        smart_str("Discipline"),
        smart_str("Event"),
        smart_str("Lastname"),
        smart_str("Firstname"),
        smart_str("Sex"),
        smart_str("YearOfBirth"),
    ])
    for obj in queryset:
        lastname = str(obj.member_id).split(" ")[0][:-1]
        firstname = str(obj.member_id).split(" ")[1]
        sex = str(obj.member_id).split(" ")[2]
        year_of_birth = str(obj.member_id).split(" ")[3]
        writer.writerow([
            # smart_str(obj.pk),
            smart_str(obj.result_value),
            smart_str(obj.discipline_id),
            smart_str(obj.event_id),
            smart_str(lastname),
            smart_str(firstname),
            smart_str(sex),
            smart_str(year_of_birth),
        ])
    return response


export_results_csv.short_description = u"Export Results CSV"
