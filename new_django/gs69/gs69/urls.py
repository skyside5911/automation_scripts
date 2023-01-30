
from django.contrib import admin
from student import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',views.setsession),
    path('get/',views.getsession),
    path('del/',views.delsession),
]
