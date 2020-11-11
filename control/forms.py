from django import forms


class SpendingForm(forms.Form):
    category = forms.CharField(max_length=50, label="Категория траты")
    costs = forms.FloatField(label="Добавка потраченной суммы")


class SalaryForm(forms.Form):
    salary = forms.FloatField(label="Ваша зарплата")