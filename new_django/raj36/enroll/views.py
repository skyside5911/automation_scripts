from django.shortcuts import render

# Create your views here.
from enroll.forms import Studentform
def fun(request):
    ff=Studentform()
    return render(request,'enroll/e1.html',{'form':ff})