from django import forms


class SpendingForm(forms.Form):
    category = forms.CharField(max_length=50)
    costs = forms.FloatField()
