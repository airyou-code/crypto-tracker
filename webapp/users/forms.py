from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import AppUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = AppUser
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
