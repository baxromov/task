from django.contrib import admin
from staff.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'position',
        'employment_date',
        'salary'
    )
