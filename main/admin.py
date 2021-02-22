from django.contrib import admin

from .models import PerformanceData

class PerformanceDataAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'pub_date')
    list_filter = ['page_name', 'pub_date']
    search_fields = ['page_name']

# Register your models here.
admin.site.register(PerformanceData, PerformanceDataAdmin)