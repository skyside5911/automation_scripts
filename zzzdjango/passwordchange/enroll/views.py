from django.shortcuts import render

# Create your views here.
from .forms import Studentregister
def Regi(request):
    if request.method=='POST':
        fm=Studentregister(request.POST)
        if fm.is_valid():
            print('name: ', fm.cleaned_data['name'])
    else:        
        fm=Studentregister()
    return render(request,'enroll/home.html',{'form':fm})