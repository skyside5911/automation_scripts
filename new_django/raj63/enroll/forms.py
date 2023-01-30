from django import forms
from .models import Student
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(forms.ModelForm):
	
	class Meta:
		model = Student
		fields = '__all__'
