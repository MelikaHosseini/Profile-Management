from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserSignUpForm(UserCreationForm):

    class Meta:
        # full_name = forms.CharField(widget=forms.TextInput(attrs = { 'placeholder' : 'Enter Full Name' , "class":"input-box"} ))
        username = forms.CharField(widget=forms.TextInput(attrs = { 'placeholder' : 'username', "class":"input-box"} ))
        email = forms.EmailField(widget=forms.TextInput(attrs = { 'placeholder' : 'Enter email', "class":"input-box"} ))
        phone = forms.CharField(widget=forms.TextInput(attrs = { 'placeholder' : 'phone' , "class":"input-box"} ))
        password = forms.CharField(widget=forms.TextInput(attrs = { 'placeholder' : 'password', "class":"input-box"} ))
        password2 = forms.CharField(widget=forms.TextInput(attrs = { 'placeholder' : 'confirm password', "class":"input-box"} ))

        model = User
        fields = ['username', 'email', 'phone','password1', 'password2'] 