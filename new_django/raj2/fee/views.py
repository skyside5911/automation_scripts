from django.shortcuts import render

# Create your views here.
def fee(request):
    return render(request,'fee/fee1.html')
def fee2(request):
    return render(request,'fee/fee2.html')