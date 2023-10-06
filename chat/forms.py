from django import forms
from .models import User

class InputForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput}