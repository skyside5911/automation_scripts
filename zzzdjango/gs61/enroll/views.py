from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from .forms import UserForm
def fun(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            messages.success(request,'created successfully')
            fm.save()
    else:        
        fm=UserForm()
    return render(request,'enroll/home.html',{'form':fm})
def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            pwd=fm.cleaned_data['password']
    login_form=AuthenticationForm()
    return render(request,'enroll/login.html',{'form':login_form})
    