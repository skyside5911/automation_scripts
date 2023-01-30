from django.contrib import admin

# Register your models here.
from .models import Student,Teacher
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','pass_date']
@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','empnum','city','salary','join_date']