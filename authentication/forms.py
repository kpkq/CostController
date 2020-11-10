from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostControlUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label="Имя")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Повторите пароль")

    class Meta:
        model = CostControlUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CostControlUser
        fields = ('username', 'email')
