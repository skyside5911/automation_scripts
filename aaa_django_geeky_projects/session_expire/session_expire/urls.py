
from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',views.getsession),
    path('set/',views.setsession),
    path('del/',views.delsession),
]
