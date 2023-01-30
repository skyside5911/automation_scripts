from django.contrib import admin
from django.urls import path
from miniblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<int:id>/',views.updatepost,name='updatepost'),
    path('delete/<int:id>/',views.deletepost,name='deletepost'),
]