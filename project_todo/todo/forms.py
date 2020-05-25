from django.forms import ModelForm
from .models import Task
from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']

class TaskUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

