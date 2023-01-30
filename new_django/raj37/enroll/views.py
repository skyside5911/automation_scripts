from django.shortcuts import render

# Create your views here.
from enroll.forms import Studentform
def fun(request):
    if request.method=='POST':
        ff=Studentform(request.POST)
        if ff.is_valid():
            print(ff.cleaned_data)
    else:
        ff=Studentform()
    return render(request,'enroll/e1.html',{'form':ff})