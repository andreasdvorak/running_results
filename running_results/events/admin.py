from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'website', 'note')

admin.site.register(Event, EventAdmin)

admin.site.site_header = "Running Results"

