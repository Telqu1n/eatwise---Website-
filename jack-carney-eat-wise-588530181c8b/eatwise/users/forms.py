from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})

        self.fields['password'].label = 'Password'
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})