from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import Userform
def sign_up(request): 
    if request.method=='POST':
        fm=Userform(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully')
            fm.save()
    else:
        fm=Userform()
    return render(request,'enroll/login.html',{'form':fm})
def user_profile(request):
    return render(request,'enroll/profile.html',{'name':request.user})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')