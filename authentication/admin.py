from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CostControlUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CostControlUser
    list_display = ['email', ]

    USERNAME_FIELD = 'email'


admin.site.register(CostControlUser, CustomUserAdmin)
