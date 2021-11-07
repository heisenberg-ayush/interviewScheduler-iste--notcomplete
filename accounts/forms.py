from django import forms
from users.models import CustomUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'reg_num', 'password1', 'password2']