from django import forms
from .models import user_id


class CRUDFORM(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "User Name"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        
        "class": "form-control",
        "placeholder": "Password"
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        
        "class": "form-control",
        "placeholder": "Gender"
    }))
    dob = forms.DateField(widget=forms.DateInput(attrs={
        
        "class": "form-control",
        "placeholder": "DOB"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        
        "class": "form-control",
        "placeholder": "email"
    }))
    
    class Meta:
        model = user_id
        fields = [
            'user_name', 'password','gender','dob','email'
        ] 