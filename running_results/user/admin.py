from django.contrib import admin

# Register your models here.

from .models import Role, User

admin.site.register(Role)
admin.site.register(User)