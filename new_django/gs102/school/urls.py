from django.contrib import admin
from django.urls import path
from school import views
urlpatterns = [
    path('',views.home)
]