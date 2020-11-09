from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import CostControlUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


def validate_form(request):
    form = CustomUserCreationForm()
    if request.method == "POST" and request.is_ajax():
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"created": True}, status=200)
        else:
            return JsonResponse({"created": False}, status=400)


