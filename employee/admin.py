from django.contrib import admin

from .models import EmployeeProfile, UploadFile

admin.site.register(EmployeeProfile)
admin.site.register(UploadFile)