from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
def sign_up(request):
    fm=UserCreationForm()
    return render(request,'enroll/e1.html',{"ff":fm})