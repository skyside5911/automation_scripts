from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('f1/',views.f1),
    path('f2/',views.f2),
]