from django.shortcuts import render

# Create your views here.
from control.forms import SpendingForm
from control.models import Spendings


def get_spendings(request):
    if request.is_ajax():
        form = SpendingForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            costs = form.cleaned_data.get("costs")
            user_spendings = Spendings.objects.get_or_create(user=request.user)
            print()
    else:
        form = SpendingForm()
    return render(request, 'home.html', {'form': form})
