from django.contrib.auth.forms import UserCreationForm
from django import forms
class Userform(UserCreationForm):
    class Meta:
        fields = ['__all__']