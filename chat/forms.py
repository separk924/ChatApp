from django import forms  

class InputForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)