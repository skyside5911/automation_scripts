from django.shortcuts import render

# Create your views here.
def setcookies(request):
    resp = render(request,'student/setcookies.html')
    resp.set_cookie('name','sonam')
    resp.set_signed_cookie('name','sonam',salt='nm',expires=datetime.utcnow()+timedelta(days=2))
    return resp
def getcookies(request):
    name=request.COOKIES.get('name')
    # name=request.COOKIES['name']
    return render(request,'student/getcookies.html',{'name':name})
def delcookies(request):
    resp = render(request,'student/delcookies.html')
    resp.delete_cookie('name')
    return resp
    