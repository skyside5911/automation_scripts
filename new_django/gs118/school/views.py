from django.shortcuts import render
from.models import Student
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
class Studentlistview(ListView):
    model=Student
    def get_queryset(self):
        return Student.objects.filter(course='Python')
    def get_context_data(self,*args, **kwargs):
        context= super().get_context_data(*args,**kwargs)
        context['freshers']=Student.objects.all().order_by('name')
        return context
    def get_template_names(self):
        if self.request.COOKIES['user']=='RAJ':
            template_name='school/stud.html'
        else:
            template_name=self.template_name
        return [template_name]