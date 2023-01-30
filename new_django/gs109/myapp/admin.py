from django.contrib import admin

# Register your models here.
from .models import Page
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat','page_publish_date','user']