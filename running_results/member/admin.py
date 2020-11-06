from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firistname', 'sex', 'year_of_birth')

admin.site.register(Member, MemberAdmin)