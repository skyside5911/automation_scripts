from django.shortcuts import render

# Create your views here.
def course1(request):
     return render(request,'course/c1.html',{'n1':'raj rana'})
def course2(request):
     return render(request,'course/c2.html',{'n2':'bantu rana'})