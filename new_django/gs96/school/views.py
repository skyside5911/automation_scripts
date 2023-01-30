from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from .models import Student,Teacher
def home(request):
    student_data=Student.objects.all()#provide all data in database
    student_data=Student.objects.exclude(marks=90)#provide excluded data from database
    student_data=Student.objects.filter(marks=90)#it filter the data and provide only filtered data from database
    student_data=Student.objects.order_by('city')#it give order to the data and show to user in ascending order
    student_data=Student.objects.order_by('-city')#it give order to the data and show to user in descending order
    student_data=Student.objects.order_by('?')#it give   data  to the user and show randomly
    student_data=Student.objects.order_by('id').reverse()[:2] #it give data in reverse order
    student_data=Student.objects.values()#it provide data in dictionary form
    student_data=Student.objects.values_list()#it provide data in tuple form 
    student_data=Student.objects.using('default')#it shows that what database you are using
    student_data=Student.objects.values_list('name','city',named=True)#it provide specific data in tuple form 
    student_data=Student.objects.values('name','city')#to get specific data in dictionary form
    student_data=Student.objects.dates('pass_date','month')#it provide data in tuple form 
    ############teacher table ##########
    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)
    student_data=qs2.union(qs1)
    ############and / or ##########
    student_data=Student.objects.filter(marks=90)& Student.objects.filter(marks=90)
    student_data=Student.objects.filter(marks=90,roll=3)
    student_data=Student.objects.filter(Q(id=90) & Q(roll=3))
    student_data=Student.objects.filter(marks=90)| Student.objects.filter(marks=90)
    student_data=Student.objects.filter(Q(id=90) | Q(roll=3))
    
    print("student data ==",student_data)
    print("student data query == ",student_data.query)
    return render(request,'school/home.html',{'students':student_data})