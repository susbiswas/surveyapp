from django.contrib import admin

# Register your models here.
from .models import Vaccination_Status,HealthIssue,Prevaccine_Health_Issue,Postvaccine_Health_Issue

admin.site.register(Vaccination_Status)
admin.site.register(HealthIssue)
admin.site.register(Prevaccine_Health_Issue)
admin.site.register(Postvaccine_Health_Issue)