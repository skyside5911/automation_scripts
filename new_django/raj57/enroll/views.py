from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .forms import StudentForm
def regi(request):
    if request.method=='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
        messages.add_message(request,messages.SUCCESS,'your account is created')
    else:
        fm=StudentForm()
    return render(request,'enroll/e1.html',{'forrrm':fm})