from django.shortcuts import render

# Create your views here.
#function base view
from django.http import HttpResponse
def myview(request):
    return HttpResponse('<h1>this is http response</h1>')
#class based view
from django.views import View
from .forms import Myform
def contactform(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("thanks")
    else:
        form= Myform()
    return render(request,'school/contact.html',{'form':form})
class MyView(View):
    def get(self,request):
        return render(request,'school/home.html')
        # return HttpResponse('<h1>this is http response</h1>')
def about(request):
    return render(request,'school/about.html')
class Myabout(View):
    def get(self,request):
        conn={'msg':'this is about page using class'}
        
        return render(request,'school/about.html',conn)

class Mycontact(View):
    def get(self,request):
        form=Myform()
        return render(request,'school/contact.html',{'form':form})
    def post(self,request):
        form=Myform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse("thanks")