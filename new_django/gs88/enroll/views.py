from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# def home(request):
#     mv = cache.get('moive','has_expired')
#     if mv == 'has_expired':
#         cache.set('movie','one',20)
#         mv=cache.get('movie')
#     return render(request,'enroll/course.html',{'fm':mv})
# def home(request):
#     mv = cache.get_or_set('fees',00,50,version=2)
    # return render(request,'enroll/course.html',{'fm':mv})
def home(request):
    data = {'name':'rani','roll':100}
    cache.set_many(data,20)
    sv=cache.get_many(data)
    return render(request,'enroll/course.html',{'stu':sv})
def home(request):
    cache.clear()
    return render(request,'enroll/course.html')
    