from django.contrib import admin
from .models import SiteStats

class SiteStatsAdmin(admin.ModelAdmin):
    list_display = ('url', 'views')

admin.site.register(SiteStats, SiteStatsAdmin)
