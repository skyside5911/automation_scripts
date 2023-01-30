from django import forms
class Studentform(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)<3:
            raise forms.ValidationError("enter the word length more than 5")
        return valname