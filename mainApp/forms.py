from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class UserRegistration(UserCreationForm):
    rating_text = models.CharField(max_length=120)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PostRequestForm(forms.ModelForm):
    class Meta:
        model = BuyerPostRequest
        fields = '__all__'