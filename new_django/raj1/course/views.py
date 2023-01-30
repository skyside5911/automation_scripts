from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return HttpResponse('this is raj')

def fun2(request):
    return HttpResponse('this is raj2')