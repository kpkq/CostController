import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from control.forms import *
from control.models import Spendings


def ajax_spending_form(request):
    if request.is_ajax():
        form = SpendingForm(request.POST)
        if form.is_valid():
            category = str(form.cleaned_data.get("category")).lower().capitalize()
            costs = form.cleaned_data.get("costs")
            if costs < 0:
                response = JsonResponse({"error": "Недопустима отрицательная сумма"})
                response.status_code = 400
                return response
            try:
                spend = Spendings.objects.get(user__email__exact=request.user.email)
                if category not in spend.info:
                    spend.info[category] = costs
                else:
                    spend.info[category] += costs
                spend.save()
                return JsonResponse(spend.info)
            except Spendings.DoesNotExist:
                Spendings(user=request.user, info={category: costs}).save()
                return JsonResponse({category: costs})


@login_required
def show_gisto(request):
    form = SpendingForm()
    info = Spendings.objects.get(user__email__exact=request.user.email).info
    return render(request, 'gisto.html', {'form': form, 'info': json.dumps(info)})


@login_required
def show_pie(request):
    if request.is_ajax():
        if "salary" in request.POST:
            spend = Spendings.objects.get(user__email__exact=request.user.email)
            salary = float(request.POST["salary"])
            if salary < 0:
                response = JsonResponse({"error": "Недопустима отрицательная сумма"})
                response.status_code = 400
                return response
            else:
                spend.salary = salary
                spend.save()
                return JsonResponse({"success": True})
    else:
        form = SalaryForm()
        spend_form = SpendingForm()
    return render(request, 'pie.html', {'form': form, 'spend_form': spend_form})
