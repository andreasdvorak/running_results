from django.contrib import admin
from django.utils.html import format_html

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'custom_url', 'note')

    def custom_url(self, obj):
        return format_html(
        '<a href="{0}" >{0}</a>&nbsp;',
            obj.website
        )
    custom_url.short_description = 'Website'
    custom_url.admin_order_field = 'website'

admin.site.register(Event, EventAdmin)

admin.site.site_header = "Running Results"

