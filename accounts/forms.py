from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
                               )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                  )
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}),\
                              )
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1', 'password2',]
