from django.shortcuts import render

# Create your views here.
from enroll.forms import Studentform
def fun(request):
    ff=Studentform(auto_id=True)
    return render(request,'enroll/e1.html',{'form':ff})