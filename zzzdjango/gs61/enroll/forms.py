from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    password1=forms.CharField(label='Main Password',widget=forms.PasswordInput)
    class Meta:
        model =User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
            