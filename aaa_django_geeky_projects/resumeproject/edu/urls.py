from django.contrib import admin
from django.urls import path,include
from edu import views
# from serv import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.home,name='homepage'),
    # path('s/',include('serv.urls')),
    path('skills/',views.Skills,name='skills'),
]