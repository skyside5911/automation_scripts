from django import forms
class Studentform(forms.Form):
    name = forms.CharField()
    city = forms.CharField()