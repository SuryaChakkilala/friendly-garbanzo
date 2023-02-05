from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    designation = forms.CharField(max_length=150)
    department = forms.CharField(max_length=150)
    organization = forms.CharField(max_length=150)
    place = forms.CharField(max_length=150)
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'designation', 'department', 'organization', 'place')

class CustomUserChangeForm(UserChangeForm):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    designation = forms.CharField(max_length=150)
    department = forms.CharField(max_length=150)
    organization = forms.CharField(max_length=150)
    place = forms.CharField(max_length=150)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'designation', 'department', 'organization', 'place')