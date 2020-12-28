from django.http import HttpResponse
from django.utils.encoding import smart_str
import csv
import logging

logger = logging.getLogger('console_file')


def export_member_csv(modeladmin, request, queryset):
    logger.debug('export member to csv')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=member_export.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        # smart_str(u"ID"),
        smart_str(u"Lastname"),
        smart_str(u"Firstname"),
        smart_str(u"Sex"),
        smart_str(u"Year of birth"),
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


export_member_csv.short_description = u"Export Member CSV"


def export_results_csv(modeladmin, request, queryset):
    logger.debug('export result to csv')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=results_export.csv'
    writer = csv.writer(response, csv.excel)
    # BOM (optional...Excel needs it to open UTF-8 file properly)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        # smart_str(u"ID"),
        smart_str(u"Result_Value"),
        smart_str(u"Discipline"),
        smart_str(u"Event"),
        smart_str(u"Lastname"),
        smart_str(u"Firstname"),
        smart_str(u"Sex"),
        smart_str(u"YearOfBirth"),
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
