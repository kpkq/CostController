import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
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
                return JsonResponse({"json_response": spend.info, "salary": spend.salary})
            except Spendings.DoesNotExist:
                Spendings(user=request.user, info={category: costs}).save()
                return JsonResponse({category: costs})


def ajax_delete_view(request):
    spend = Spendings.objects.get(user__email__exact=request.user.email)
    del spend.info[request.POST["category"]]
    print(spend.info)
    print(spend.salary)
    spend.save()
    return JsonResponse({"json_response": spend.info, "salary": spend.salary})


def ajax_change_spending(request):
    spend = Spendings.objects.get(user__email__exact=request.user.email)
    if request.POST["category"] != request.POST["changed"]:
        del spend.info[request.POST["changed"]]
        spend.info[request.POST["category"]] = request.POST["costs"]
    spend.save()
    return JsonResponse({"json_response": spend.info, "salary": spend.salary})


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
                return JsonResponse({"salary": salary, "spent": spend.info})
    else:
        form = SalaryForm()
        spend_form = SpendingForm()
        change_spending_form = ChangeSpendingForm()
        spending = Spendings.objects.get(user__email__exact=request.user.email)
    return render(request, 'pie.html', {'form': form, 'spend_form': spend_form, 'change_spending_form': change_spending_form,
                  'info': json.dumps(spending.info), 'salary': spending.salary})
