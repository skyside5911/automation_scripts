from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('coo/',views.course),
    path('coo2/',views.course2),
]