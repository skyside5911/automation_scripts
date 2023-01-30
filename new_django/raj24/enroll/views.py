from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def Stuview(request):
    studd=Student.objects.all()
    return render(request,'enroll/studentt.html',{'st':studd})