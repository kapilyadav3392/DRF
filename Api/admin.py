from django.contrib import admin
from .models import Section, Student

# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll', 'city']
    

@admin.register(Section)
class Sectionadmin(admin.ModelAdmin):
    list_display = ['id','section']

# admin.site.register(Student)
# admin.site.register(Section)

    