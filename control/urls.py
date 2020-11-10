from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from control.views import get_spendings

urlpatterns = [
    path('', get_spendings, name='get_spendings'),
    ]