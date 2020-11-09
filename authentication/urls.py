from django.urls import path
from .views import SignUpView, validate_form

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('validate', validate_form, name='validate'),
]