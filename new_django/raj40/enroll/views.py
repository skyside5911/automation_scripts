from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from enroll.forms import Studentform
 
def fun(request):
    if request.method=='POST':
        ff=Studentform(request.POST)
        if ff.is_valid():
            print("data is valid")
            print("name ", ff.cleaned_data['name'])
            
    else:
        ff=Studentform()
    return render(request,'enroll/e1.html',{'form':ff})