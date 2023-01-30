from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sign_up/',views.register,name='sign'),
    path('login/',views.login_page),
    path('profile/',views.profile),
]