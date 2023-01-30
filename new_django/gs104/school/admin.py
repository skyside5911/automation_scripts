from django.contrib import admin

# Register your models here.
from .models import Examcenter,MyExamcenter
@admin.register(Examcenter)
class ExamAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']
@admin.register(MyExamcenter)
class MyExamAdmin(admin.ModelAdmin):
    list_display=['id','cname','city']