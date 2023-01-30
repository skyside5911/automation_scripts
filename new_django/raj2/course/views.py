from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request,'course/course1.html',{'nm':'raj rana'})
def course2(request):
    return render(request,'course/course2.html',{'nm2':'bantu rana'})