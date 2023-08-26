from django.contrib import admin
from .models import Student

# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'field_of_study',  'year_of_study' ]
    list_filter = ['field_of_study', 'year_of_study']
