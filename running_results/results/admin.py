from django.contrib import admin

from .models import Result

class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_value','get_distance_name')

    def get_distance_name(self, obj):
        return obj.distances.name
    get_distance_name.short_description = 'Distance Name'

admin.site.register(Result,ResultAdmin)