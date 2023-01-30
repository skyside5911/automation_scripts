from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def setsession(request):
    request.session['name']='raj'
    return render(request,'student/setsession.html')
def getsession(request):
        name = request.session['name']
        return render(request,'student/getsession.html',{'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')
    
    