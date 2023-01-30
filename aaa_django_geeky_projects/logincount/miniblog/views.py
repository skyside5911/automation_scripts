from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import Signup,Loginform,Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.core.cache import cache
from django.contrib.auth.models import Group
#Home
def home(request):
    form=Post.objects.all()
    return render(request,'miniblog/home.html',{'forms':form})
def about(request):
    return render(request,'miniblog/about.html')
def contact(request):
    return render(request,'miniblog/contact.html')
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ct=cache.get('count',version=user.pk)
        return render(request,'miniblog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps,'ct':ct})
    else:
        return HttpResponseRedirect('/login/')
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=Loginform(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'login ho gya hai')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=Loginform()
        return render(request,'miniblog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
def signup(request):
    if request.method == "POST":
        form=Signup(request.POST)
        if form.is_valid():
            messages.success(request,"now you are signup")
            user =form.save()
            group= Group.objects.get(name='Author')
            user.groups.add(group)
            form=Signup()
    else:
        form=Signup()
    return render(request,'miniblog/signup.html',{'form':form})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def addpost(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form=Postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                form=Postform()
        else:
            form=Postform()
        return render(request,'miniblog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=Postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=Postform(instance=pi)
        return render(request,'miniblog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')