from django.contrib import admin
from django.urls import path
from serv import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('services/',views.services,name='services')
]