from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import StudentModel
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.
from django.views import View
class UserAddshowview(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(**kwargs)
        formm = StudentForm()
        stu = StudentModel.objects.all()
        context = {'forrm':formm,'student':stu}
        return context
    def post(self,request):
        formm = StudentForm(request.POST)
        if formm.is_valid():
            name = formm.cleaned_data['name']
            email = formm.cleaned_data['email']
            password = formm.cleaned_data['password']
            reg = StudentModel(name=name,email=email,password=password)
            reg.save()
            return HttpResponseRedirect('/')

class DeleteView(RedirectView):
    url=('/')
    def get_redirect_url(self, *args, **kwargs):
        id=kwargs['id']
        StudentModel.objects.get(pk=id).delete()
        return super().get_redirect_url(*args, **kwargs)
class UpdateView(View):
    def get(self,request,id):
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':formm})
    def post(self,request,id):
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(request.POST,instance=pi)
        if formm.is_valid:
            formm.save()
        return render(request,'enroll/updatestudent.html',{'form':formm})
            
            
        
'''def updat(request,id):
    if request.method == 'POST':
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(request.POST,instance=pi)
        if formm.is_valid:
            formm.save()
            formm = StudentForm()
            
    else:
        pi = StudentModel.objects.get(pk=id)
        formm = StudentForm(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':formm})'''