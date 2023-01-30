from django.contrib import admin

# Register your models here.
from .models import Examcenter,Student
@admin.register(Examcenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','cname','city','name','roll']