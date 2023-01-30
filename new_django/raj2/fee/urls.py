from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('fe/',(views.fee)),
    path('fe1/',(views.fee2)),
]