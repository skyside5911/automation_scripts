
from django.contrib import admin
from django.urls import path
from enroll import views
urlpatterns = [
    path('',views.fun,name='fun'),
    path('login/',views.user_login,name='user_login')
]