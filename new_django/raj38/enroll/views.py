from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from enroll.forms import Studentform
def thankyou(request):
    return render(request,'enroll/e2.html',)
def fun(request):
    if request.method=='POST':
        ff=Studentform(request.POST)
        if ff.is_valid():
            name= (ff.cleaned_data['name'])
        return HttpResponseRedirect('/regi/success')
        # return render(request,'enroll/e2.html',{'forrm':name})
            
    else:
        ff=Studentform()
    return render(request,'enroll/e1.html',{'form':ff})