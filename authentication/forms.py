from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostControlUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CostControlUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CostControlUser
        fields = ('username', 'email')
