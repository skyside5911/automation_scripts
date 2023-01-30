from django.shortcuts import render

# Create your views here.
from .models import Student
def home(request):
    student_data=Student.objects.all()
    student_data=Student.objects.filter(name__exact='RAJ')
    student_data=Student.objects.filter(name__iexact='RAJ')
    student_data=Student.objects.filter(name__contains='RAJ')
    
    print('return data',student_data)
    print()
    print('sql query: ',student_data.query)
    return render(request,'school/home.html',{'students':student_data})