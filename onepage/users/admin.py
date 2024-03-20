from django.contrib import admin
from .models import AppUser, AppUserSettings

admin.site.register(AppUser)
admin.site.register(AppUserSettings)
