from course import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('info/',views.django,name='djangoo'),
]