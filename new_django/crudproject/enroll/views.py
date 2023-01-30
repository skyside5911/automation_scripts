from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import StudentModel
# Create your views here.
def project(request):
    if request.method == 'POST':
        formm = StudentForm(request.POST)
        if formm.is_valid():
            name = formm.cleaned_data['name']
            email = formm.cleaned_data['email']
            password = formm.cleaned_data['password']
            reg = StudentModel(name=name,email=email,password=password)
            reg.save()
            formm = StudentForm()
            
    else:
        formm = StudentForm()
    stu = StudentModel.objects.all()
        
    return render(request,'enroll/addandshow.html',{'forrm':formm,'student':stu})
def del_data(request,id):
    if request.method=='POST':
        pi = StudentModel.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def updat(request,id):
    if request.method == 'POST':
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(request.POST,instance=pi)
        if formm.is_valid:
            formm.save()
    else:
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':formm})