from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from .models import Student,Teacher
def home(request):
    student_data=Student
    print("student data ==",student_data)
    print("student data query == ",student_data.query)
    return render(request,'school/home.html',{'students':student_data})