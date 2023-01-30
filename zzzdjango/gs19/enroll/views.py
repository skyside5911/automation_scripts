from django.shortcuts import render
from .models import User
# Create your views here.
from .forms import Studentregister
def Regi(request):
    if request.method=='POST':
        fm=Studentregister(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['pwd']
            reg=User(name=nm,email=em,password=pwd)
            reg.save()
    else:        
        fm=Studentregister()
    return render(request,'enroll/home.html',{'form':fm})