from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from enroll.forms import Studentform
from .models import Student
from .forms import Studentform,Teacherform
def fun(request):
    if request.method=='POST':
        ff=Studentform(request.POST)
        if ff.is_valid():
            ff.save()
            
    else:
        ff=Studentform()
    return render(request,'enroll/e1.html',{'form':ff})
def teacher_fun(request):
    if request.method=='POST':
        ff=Teacherform(request.POST)
        if ff.is_valid():
            ff.save()
            
    else:
        ff=Teacherform()
    return render(request,'enroll/e2.html',{'form':ff})