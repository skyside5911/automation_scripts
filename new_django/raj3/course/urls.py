from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('c1/',views.course1),
    path('c2/',views.course2),
]