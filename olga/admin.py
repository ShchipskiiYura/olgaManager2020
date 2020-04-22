from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmpoyeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass