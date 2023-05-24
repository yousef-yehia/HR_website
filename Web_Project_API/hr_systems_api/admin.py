from django.contrib import admin
from hr_systems_api import models
# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Vacation)
