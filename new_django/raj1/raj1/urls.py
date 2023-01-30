
from django.contrib import admin
from django.urls import path,include
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun/',views.fun),
    path('fun2/',views.fun2),
]
