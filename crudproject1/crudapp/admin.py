from django.contrib import admin
from crudapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['Sno','Name','Age','Dep']
admin.site.register(Student,StudentAdmin)
# Register your models here.
