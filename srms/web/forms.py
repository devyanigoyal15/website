from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class UserRegistrationForm(UserCreationForm):
    name = forms.CharField()
    dob = forms.CharField()
    gender = forms.CharField()
    address = forms.CharField()
    email=forms.EmailField()
    desg = forms.CharField()

    class Meta:
        model=User
        fields=['username','name','dob','gender','address','email','password1','password2']