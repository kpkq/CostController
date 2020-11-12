from django.contrib import admin
from django.urls import path

from control.views import *

urlpatterns = [
    path('gisto', show_gisto, name='gisto'),
    path('pie', show_pie, name='pie'),
    path('ajax_request', ajax_spending_form, name='ajax_request'),
    path('delete_category', ajax_delete_view, name='ajax_delete'),
    path('change_spending', ajax_change_spending, name='ajax_change')
    ]