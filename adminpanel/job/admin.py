from django.contrib import admin
from .models import *
from job.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title','company_name','City','total_salary')
    search_fields = ('job_title','company_name','City')
    
admin.site.register(Job,JobAdmin)

