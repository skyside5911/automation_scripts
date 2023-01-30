from django import forms
from .models import Student
class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields =['studentname','email','password']
class Teacherform(Studentform):
    class Meta(Studentform.Meta):
        fields =['teachername','email','password']
        