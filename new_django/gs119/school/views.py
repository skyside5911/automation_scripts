from django.shortcuts import render
from.models import Student
# Create your views here.
from django.views.generic.list import ListView
class Studentlistview(ListView):
    model=Student
    