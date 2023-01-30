from django.core import validators
from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'})
        }