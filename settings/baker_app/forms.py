from fileinput import FileInput
from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms import ImageField, ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class NewUserForm(UserCreationForm):
    email= forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username" , "email" , "password1" , "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
            return user

def __init__(self, *args, **kwargs):
    super(NewUserForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'
