from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,'fee/f1.html',{'f1':'fee of python'})
def f2(request):
    return render(request,'fee/f2.html',{'f1':'fee of django'})