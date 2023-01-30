from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . import forms


def login_page(request):
    # form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user!=None:
                login_page(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll/login.html', context={'form': form})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'account create sucessfully')
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
    else:
            messages.info(request, f'account done not exit plz sign in')
            form = UserRegisterForm()
    return render(request, 'enroll/e1.html', {'form':form})
def profile(request):
    return render(request,'enroll/profile.html')