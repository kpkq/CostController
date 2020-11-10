import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from control import models
from control.forms import SpendingForm
from control.models import Spendings


@login_required
def get_spendings(request):
    if request.is_ajax():
        form = SpendingForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            costs = form.cleaned_data.get("costs")
            print(category + " " + str(costs))
            try:
                spend = Spendings.objects.get(user__email__exact=request.user.email)
                if category not in spend.info:
                    spend.info[category] = costs
                else:
                    spend.info[category] += costs
                print(spend.info)
                spend.save()
                return JsonResponse(spend.info)
            except Spendings.DoesNotExist:
                Spendings(user=request.user, info={category: costs}).save()
                return JsonResponse({category: costs})

    else:
        form = SpendingForm()
        info = Spendings.objects.get(user__email__exact=request.user.email).info
        print(type(json.dumps(info)))
        print(json.dumps(info))
    return render(request, 'home.html', {'form': form, 'info': json.dumps(info)})
