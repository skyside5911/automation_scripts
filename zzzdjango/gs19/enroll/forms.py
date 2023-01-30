from django import forms
class Studentregister(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter Your Name'})
    email=forms.EmailField(error_messages={'required':'Enter Your Email'})
    pwd=forms.CharField(widget=forms.PasswordInput)
    '''rpwd=forms.CharField(label='confirm Password', widget=forms.PasswordInput)
    def clean(self):
        cleaned_data= super().clean()
        valpwd=self.cleaned_data['pwd']
        valrpwd=self.cleaned_data['rpwd']
        if valpwd!=valrpwd:
            raise forms.ValidationError("password does not match")'''